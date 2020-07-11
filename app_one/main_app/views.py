from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseRedirect, JsonResponse
from main_app.models import team,service,contact_setting,slider, aboutUs
from django.core.urlresolvers import reverse
from . import forms
from main_app.models import message
from django.core.mail import send_mail

# Create your views here.


def index(request):
    # links and setup
    # main_settings = main_setting.objects.order_by('id')
    about_module = aboutUs.objects.order_by('id')
    slider_module = slider.objects.order_by('id')
    services_modeule = service.objects.order_by('id')
    cs_module = contact_setting.objects.order_by('id')
    team_module = team.objects.order_by('id')
    photo_path = 'assets/img/slider/'
    t_photo_path = 'assets/img/team/'
    form = forms.ContactUs()
    web_dict = {'slider':slider_module,'aboutus':about_module,'services':services_modeule,'contact_setting':cs_module,'team':team_module,'p_path':photo_path, 'form': form,'t_p_path':t_photo_path}
    return render(request,'main_app/index.html',context = web_dict)

def message_validator(request):
    if request.method == 'POST':
        name = request.POST['name']
        myemail = request.POST['email']
        subject = request.POST['subject']
        myMessage= request.POST['message']
        recipient_list = [myemail]
    
        send_mail( subject, myMessage, myemail, recipient_list, fail_silently=False )
        message.objects.create(
            name = name,
            email = myemail,
            subject = subject,
            message= myMessage
        )
    
        return HttpResponse('Message Sent')
    
def sliders(request):
    slider_module = slider.objects.order_by('id')
    
    slide_dict = {'sliders':slider_module,}
    return render(request,'main_app/admin_slider.html', context=slide_dict)

def add_slider(request):
    if request.method == 'POST':
        slider_name = request.POST['slider_name']
        slider_no = request.POST['slider_no']
        contentOneVal = request.POST['contentOne']
        contentTwoVal = request.POST['contentTwo']
        slider_image = request.POST['slider_image']
        statusVal = request.POST['status']
        image_file = request.FILES['image_file']
        slider.objects.create(
            name = slider_name,
            FileName = slider_image[12:],
            ContentOne = contentOneVal,
            ContentTwo = contentTwoVal,
            SliderNo = slider_no,
            status = statusVal,
            myImage = image_file,
            )

        return HttpResponse('Saved')
def edit_slider(request):
    if request.method == 'POST':
        slider_id = request.POST['edit_slider_id']
        slider_name = request.POST['edit_slider_name']
        slider_no = request.POST['edit_slider_no']
        contentOneVal = request.POST['edit_contentOne']
        contentTwoVal = request.POST['edit_contentTwo']
        slider_image = request.POST['edit_slider_image'][12:]
        statusVal = request.POST['edit_status']
        
        
        if not slider_image == '':
            MyNewSlide = slider.objects.get(id = slider_id)
            image_file = request.FILES['image_file']
            MyNewSlide.name = slider_name
            MyNewSlide.SliderNo = slider_no
            MyNewSlide.ContentOne = contentOneVal
            MyNewSlide.ContentTwo = contentTwoVal
            MyNewSlide.FileName = slider_image
            MyNewSlide.status = statusVal
            MyNewSlide.myImage = image_file
            MyNewSlide.save()
            # return redirect('/sliders/#tab_2?success')
            return HttpResponse('Updated')
            

        else:
            MyNewSlide = slider.objects.get(id = slider_id)
            image_file = request.FILES
            MyNewSlide.name = slider_name
            MyNewSlide.SliderNo = slider_no
            MyNewSlide.ContentOne = contentOneVal
            MyNewSlide.ContentTwo = contentTwoVal
            MyNewSlide.status = statusVal
            MyNewSlide.save()
            # return redirect('/sliders/#tab_2?success')
            return HttpResponse('Updated')
            
def list_slider(request):
    slider_module = slider.objects.order_by('id')
    web_dict = {'sliders': slider_module}
    return render(request,'main_app/display_slider.html',context=web_dict)


def services(request):
    return render(request,'main_app/admin_services.html')

def aboutus(request):
    return render(request, 'main_app/admin_aboutus.html')