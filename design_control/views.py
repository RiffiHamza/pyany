from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import (
    base_design_control,
    index_design_control,
    price_table_control,
    about_design_control,
    Index_botem_Slider,
    contact_design_control)
from availability.models import Availability
import requests
# Create your views here.







# Get Desig Data From DataBase to BASE.HTML


####------------------Bothm Slider---------------------##


####------------------End---------------------##
def design_data_base(req):
    connstatt='login'
    if 'online' in req.session:
        coonbtn="logout"
    else:
        coonbtn="login"
    
    objavb=Availability.objects.all()
    obj = base_design_control.objects.get(id=1)
    obj2=index_design_control.objects.get(id=1)
    obj_price =price_table_control.objects.all()
    obj_about_info=about_design_control.objects.get(id=1)
    bothm_slider=data=Index_botem_Slider.objects.all()
    
    context = {
        'nav_location_addres': obj.nav_location_addres,
        'nav_email_addres': obj.nav_email_addres,
        'nav_facebook_addres': obj.nav_facebok_addres,
        'nav_main_button': obj.nav_main_button,
        'nav_link_titel1': obj.nav_link_titel1,
        'nav_link_titel2': obj.nav_link_titel2,
        'nav_link_titel3': obj.nav_link_titel3,
        'nav_link_titel4': obj.nav_link_titel4,
        'nav_link_titel5': obj.nav_link_titel5,
        'nav_link_titel6': obj.nav_link_titel6,
        'nav_link_titel7': obj.nav_link_titel7,
        'main_title1':obj2.slaid_taitle_main_1,
        'sub_title1':obj2.slaid_sub_taitle_1,
        'loginbtn':coonbtn,
        'seginupbtn':'Seginup',
        'connstatt':connstatt,
        ####------------------PRICE Data---------------------##
        'my_list':obj_price,
        ####------------------about Data---------------------##
        'about_list':obj_about_info,
        'bothm_slider':bothm_slider,
         ####------------------Contact Page ---------------------##
        'contact_data':contact_design_control.objects.get(id=1),
        ####------------------Availability Page ---------------------##
        'avb':objavb


    }
    return context


# Home View


def home_view(req):
   
    
    context_base = design_data_base(req)
    return render(req, 'index.html', context_base)

# About View


def about_view(req):
    context_base = design_data_base(req)
    return render(req, 'about.html', context_base)

# Contact  View


def contact_view(req):
    context_base = design_data_base(req)

    return render(req, 'contact.html', context_base)

# Service View


def service_view(req):
    context_base = design_data_base(req)
    return render(req, 'service.html', context_base)

# Pricing View


def pricing_view(req):
    context_base = design_data_base(req)

    return render(req, 'pricing.html', context_base)

# Blog View


def blog_view(req):
    context_base = design_data_base(req)

    return render(req, 'blog.html', context_base)





