from django.shortcuts import render, redirect
from .models import Medicine
from .forms import MedicineForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# User Authentication
def Signup(request):
    if request.method == 'POST':
        name = request.POST['username']                                                                                                                  # request.POST attribute has the data of the submitted form by the user using POST method.
        pass_word = request.POST['password']

        if User.objects.filter(username=name).exists():
            messages.info(request,'Error : User already exists')                                                                                            #Django messages framework sends the messages to the server with the request and stored in Sessions.
            return redirect('signup')
        else :
            user = User.objects.create_user(username=name, password=pass_word)
            user.save()                                                                                                                 #saves an instance of user into the database 
            messages.info(request,'User Created Succesfully!') 
            return redirect('list')
    else:
      return render(request,'registration/signup.html')
    
    
def Login(request): 
        if request.method == 'POST':
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user= auth.authenticate(username=user_name,password=pass_word)
                                                                                                                                                            # authenticate() validates the username and pass with the datebase
            
            if user is not None:
                auth.login(request,user)                                                                                 #auth.login() creates and saves an user sessionID in the server. (session ID is sent to browser as response and saved as a cookie.)
                return redirect('list')
            else:
                messages.info(request,'Error : invalid credentials') 
                return redirect('login')
        else:
            return render(request,'registration/login.html')
        
@login_required        
def Logout(request):
    auth.logout(request)                                                                                             # auth.logout() clears the current user's session ID
    return render(request,'registration/logout.html')

# CRUD
@login_required
def List(request):

    if 'q' in request.GET:
        q=request.GET['q']
        meds=Medicine.objects.filter(name__icontains=q) 
                                                                                                                    #The __icontains is a lookup, that means the search is case-insensitive and will match partial words. Its used to retrieve a something from a database.
    else:  
      meds= Medicine.objects.all()                              
    return render(request,"list.html",{'meds':meds})                

@login_required
def Create(request):  
    if request.method == "POST":  
        form = MedicineForm(request.POST)  #                                                                         the data in the POST request binds with the forms in MedicalForm.
        if form.is_valid():  # form validation
                form.save()
                return redirect('/')            
    else:  
        form = MedicineForm()
    return render(request,'create.html',{'form':form})  

@login_required
def Update(request, id):  
    med = Medicine.objects.get(id=id)                                                                                    # retriving the medicine from database by its id matching.
    form = MedicineForm(initial={'name': med.name,'expiry_date': med.expiry_date})  
                                                                                                                         # pre-fills the form with the data retrived in 'meds'.
                                                                                                                         # "initial" parameter set the initial values for the form fields.
                                     
    if request.method == "POST":  
        form = MedicineForm(request.POST, instance=med)
                                                                                                                          # The instance parameter is used when we want to update an existing record from the database.
                                                                                                                          # When the form is submitted, the 'instance=meds' parameter ensures that the updated data is saved to the correct "Medicine" model in the database.
        if form.is_valid():  
            form.save()
        return redirect('/')
    
    else:
     return render(request,'update.html',{'form':form})  

@login_required
def Delete(request,id):
    med = Medicine.objects.get(id=id)
    med.delete()
    return redirect('/')
