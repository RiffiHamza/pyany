from django.db import models

# Create your models here.

####-------Nav_base_Design_Model------##


class base_design_control(models.Model):
    nav_location_addres = models.CharField(max_length=50)
    nav_email_addres = models.CharField(default='No Email', max_length=50)
    ####-------Sociel_MIDea PArt------##
    nav_facebok_addres = models.CharField(max_length=50)
    nav_twitter_addres = models.CharField(default='No twitter',max_length=50)
    nav_google_addres = models.CharField(default='No Goole',max_length=50)
    nav_linkedin_addres = models.CharField(default='No LinkedIn',max_length=50)
    nav_pintrest_addres = models.CharField(default='No No Pintrest',max_length=50)
    ####-------------End--------------------##
    nav_main_button = models.CharField(max_length=50)
    nav_link_titel1 = models.CharField(max_length=50)
    nav_link_titel2 = models.CharField(max_length=50)
    nav_link_titel3 = models.CharField(max_length=50)
    nav_link_titel4 = models.CharField(max_length=50)
    nav_link_titel5 = models.CharField(max_length=50)
    nav_link_titel6 = models.CharField(max_length=50)
    nav_link_titel7 = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Navegation Bar'
        verbose_name_plural = 'Navegation Bar'

   ####-------Index_Design_Model------##


class index_design_control(models.Model):
    slaid_taitle_main_1 = models.CharField(max_length=250)
    slaid_sub_taitle_1 = models.CharField(max_length=250)
    slaid_taitle_main_2 = models.CharField(max_length=250)
    slaid_sub_taitle_2 = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'index page'
        verbose_name_plural = 'index page'

   ####-------Price_Design_Model------##


class price_table_control(models.Model):
    Service_Names = models.CharField(max_length=50)
    Stage = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Detail = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'price table'
        verbose_name_plural = 'Price Table'

   ####-------About_Design_Model------##


class about_design_control(models.Model):
    about_title = models.CharField(max_length=50)
    main_text = models.TextField()

    class Meta:
        verbose_name = 'About page'
        verbose_name_plural = 'About page'

   ####-------Footer_designe_Model------##


class footer_design_control(models.Model):
    footer_main_text = models.TextField()
    footer_phone = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Foroter information'
        verbose_name_plural = 'Foroter informations'


    ####-------Index_botem_Slider_Contant------##

text_def="i'd been avoiding the dentist for years due to bad experiences. A reminder SMS is sent the working day beforehand. I also had a call confirming appointment. I have been a patient ever since. My dentist is very reassuring andvery helpful. Excellent treatment and advice."

class Index_botem_Slider(models.Model):
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    main_text=models.TextField(default=text_def)
    name=models.CharField(max_length=50)
    class Meta:
        
        verbose_name = 'Bothem slider'
        verbose_name_plural = 'Bothem sliders'

        ####-------Contact_page_design_control------##

class contact_design_control(models.Model):
    maps_url=models.TextField()
    cart_addres=models.CharField(max_length=50)
    cart_phone=models.CharField(max_length=50)
    cart_fax=models.CharField(max_length=50)
    cart_email=models.CharField(max_length=50)
    class Meta:
        verbose_name='Contact Page Designe'
        verbose_name_plural='Contact Page Designe'
  
    