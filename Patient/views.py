
from django.shortcuts import render,redirect

from design_control.views import design_data_base

# Create your views here.
def Patient_Profile_View(req):
    if 'online' in  req.session:
        context_base = design_data_base(req)
        return render(req,'Patient_Profile.html',context_base)
    else:
        return redirect('/login')