from django.db import models

# Create your models here.
class slider(models.Model):
    name = models.CharField(max_length=264)
    FileName = models.CharField(max_length=264)
    myImage = models.FileField(null=True, upload_to='slider',  blank = True)
    ContentOne = models.CharField(max_length=200)
    ContentTwo = models.TextField(max_length=1000)
    SliderNo = models.IntegerField()
    status = models.IntegerField()
    def __str__(self):
        return  self.name

class aboutUs(models.Model):
    companyName = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length=120)
    para = models.TextField()
    checklist1 = models.CharField(max_length=50)
    checklist2 = models.CharField(max_length=50)
    checklist3 = models.CharField(max_length=50)
    checklist4 = models.CharField(max_length=50)
    checklist5 = models.CharField(max_length=50)
    checklist6 = models.CharField(max_length=50)
    checklist7 = models.CharField(max_length=50)
    checklist8 = models.CharField(max_length=50)
    def __str__(self):
        return self.companyName

class team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.CharField(max_length=100)
    facebook = models.CharField(max_length=70, unique=True)
    twitter = models.CharField(max_length=70, unique=True)
    instagram = models.CharField(max_length=70, unique=True)
    photo = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.name

class service(models.Model):
    service_photo = models.CharField(max_length=264, unique=True)
    serviceName = models.CharField(max_length=264, unique=True)
    serviceDescription = models.TextField(max_length=1000)
    serviceStatus = models.IntegerField()
    def __str__(self):
        return self.serviceName

class contact_setting(models.Model):
    contactNo = models.CharField(max_length=40, unique=True)
    emailAddress = models.CharField(max_length=70, unique=True)
    officeAvailability = models.CharField(max_length=50)
    websiteName = models.CharField(max_length=100, unique=True)
    GoogleMap = models.TextField(null=True)
    companyName = models.CharField(max_length=120, null=True)
    content = models.TextField(max_length=1000, null=True)
    facebook = models.CharField(max_length=264, null=True)
    twitter = models.CharField(max_length=264, null=True)
    instagram = models.CharField(max_length=264, null=True)
    information_cont = models.TextField(max_length=1000, null=True)
    tel_no = models.CharField(max_length=20, null=True)
    working_hours = models.CharField(max_length=20, null=True)
    cright_company = models.CharField(max_length=40, null=True)
    def __str__(self):
        return self.emailAddress

class message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    def __str__(self):
        return self.subject
    