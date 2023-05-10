
from django.urls import path
from .views import  AddMedicine,ListMedicine, MedicineDelete, MedicineSearch, MedicineUpdate




urlpatterns = [
   
     path('add-medicine/',AddMedicine.as_view(),name='add-medicine' ), 
     path('view-medicine/',ListMedicine.as_view(),name='view-medicine' ), 
     path('update/<int:pk>', MedicineUpdate.as_view(), name="Medicine-update"),
     path('delete/<int:id>', MedicineDelete.as_view(), name="medicine-delete"),
     path('', MedicineSearch.as_view(),name='search'), 
]
