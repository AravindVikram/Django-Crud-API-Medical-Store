from datetime import datetime
from django.http import Http404
from .models import medicine
from rest_framework import status
from rest_framework import  permissions
from rest_framework.views import APIView
from .serializers import MedicineSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication


class ListMedicine(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get(self,request):
        obj= medicine.objects.all()
        serialzier = MedicineSerializer(obj, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)
    
class AddMedicine(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            company = request.data.get('company')
            confirm_company = request.data.get('confirm_company')
            if company != confirm_company:
                return Response({'error': 'The company and confirm_company fields must match.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'New Medicine has been Created Successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MedicineDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self,request,id):    
        try:
            obj = medicine.objects.get(id=id)
        except medicine.DoesNotExist:
            msg = {"msg":"Medicine was not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({ "msg":"medicine was deleted"}, status=status.HTTP_204_NO_CONTENT)
    


class MedicineUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):                                                                             #The get_object method is a helper method that retrieves the medicine object with the given pk (primary key)
        try:
            return medicine.objects.get(pk=pk)
        except medicine.DoesNotExist:
            raise Http404

    def get(self, pk):
        med = self.get_object(pk)
        serializer = MedicineSerializer(med)
        return Response(serializer.data)

    def put(self, request, pk):
        med = self.get_object(pk)
        serializer = MedicineSerializer(med, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# search methord
 
class MedicineSearch(ListAPIView):
     authentication_classes = [TokenAuthentication]
     permission_classes = [permissions.IsAuthenticated]
     
     queryset = medicine.objects.all()
     serializer_class = MedicineSerializer
     filter_backends = (DjangoFilterBackend,SearchFilter)
     search_fields = ['name']         
          


