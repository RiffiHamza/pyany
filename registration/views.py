from django.shortcuts import render, redirect
from design_control.views import design_data_base
from Patient.models import Patients

# Create your views here.


def registration_View(req):
    print('Methode'+req.method)
    if req.method == 'POST':
        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        dob = req.POST.get('dob')
        gender = req.POST.get('gender')
        password = req.POST.get('password')
        try:
            objtest = Patients.objects.get(Email=email)
            return render(req,'registration.html',{'messageerror':"Accounte Exsiste"})
        except Patients.DoesNotExist as error:
            print("### You Can Register Account Not Existe ####")
            objset = Patients.objects.create(First_Name=firstname, Last_Name=lastname,
                                             Phone=phone, Email=email, gender=gender, D_Of_B=dob, Password=password)
            return redirect('/Ymkan')
    else:

        print('methode Get')
        conetxt = design_data_base(req)
        return render(req, 'registration.html', conetxt)
