from django.shortcuts import render ,  redirect
from .models import UserDetails

# Create your views here.
def index(request):
    return render(request, 'index.html')
def form(request):
    if request.method == 'POST':
        full_name = request.POST.get('fnam')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        password = request.POST.get('password')
    
        gender = request.POST.get('gender')

        if gender == 'male':
             gendervalue = 'male'
        elif gender == 'female':
            gendervalue = 'female'
        else:
            gendervalue = 'other'
            
        userdetails = UserDetails(firstName = full_name , userName = username , email =email , phoneNumber =  phone_number ,  password = password , Checkbox = gendervalue)
        userdetails.save()
        return redirect("/table")
    return render(request, 'form.html')  
def table(request):
    userdata = UserDetails.objects.all()
    
    return render(request, 'table.html', {"userdata": userdata})   
def delete(request , id):
    details = UserDetails.objects.get(id=id)
    details.delete()
    return redirect("/table")

def Edit(request, id):
    details = UserDetails.objects.get(id=id)
    return render (request, 'retrive.html' , {"details": details})

def update(request , id):
    details = UserDetails.objects.get(id=id)
    if request.method == 'POST' :
        details.firstName = request.POST['fnam']
        details.userName = request.POST['uname']
        details.email = request.POST['email']
        details.phoneNumber = request.POST['number']
        details.password = request.POST['password']
        details.Checkbox = request.POST['gender']
        details.save()
        return  redirect ("/table")
    
    
             