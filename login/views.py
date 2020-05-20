from django.shortcuts import render, redirect
from design_control.views import design_data_base
from Patient.models import Patients
from django.contrib.sessions.models import Session

# Create your views here.
# Login View


def Login_View(request):
    if request.method == "POST":
        Emailreq = request.POST.get('Email')
        password = request.POST.get('pass')
        print(str(Emailreq)+'====>'+str(password))
        try:
            obj = Patients.objects.get(Email=Emailreq)
            print('Existe')
            if password == obj.Password:
                print('Seem Password And Email')
                request.session["online"] = "online"
                return redirect('/patient_profile')

            else:
                print('Note Seeem Password ANd Email')
                return redirect('/login')

        except Patients.DoesNotExist as error:
            print('Not Existe')
            return redirect('/login')

    else:
        context = design_data_base(request)
        return render(request, 'Login.html', context)

# LogOut Function


def Logout_View(req):

    for s in Session.objects.all():
        s.delete()

    return redirect('/index')
