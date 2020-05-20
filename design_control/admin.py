from django.contrib import admin
from .models import (
    base_design_control,
    index_design_control,
    price_table_control,
    about_design_control,
    footer_design_control,
    Index_botem_Slider,
    contact_design_control)

# Register your models here.
####-------Nav_Base_Admin_Register------##
admin.site.register(base_design_control)
####-------Index_Admin_Register------##
admin.site.register(index_design_control)
####-------Price_Admin_Register------##
admin.site.register(price_table_control)
####-------About_Admin_Register------##
admin.site.register(about_design_control)
####-------Footer_Admin_Register------##
admin.site.register(footer_design_control)
####-------Admin_Register_Bohem_slider------##
admin.site.register(Index_botem_Slider)
####-------Admin_Register_Contact_page------##
admin.site.register(contact_design_control)
####-------Admin_Register_Panel_Designe------##
admin.site.site_header = 'Doctoor Panel COntrol'
admin.site.site_title = 'Welcom Admin'
