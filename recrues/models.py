from django.conf import settings
from django.db import models
from uuid import uuid4

# Create your models here.


class UsersN(models.Model):
    name = models.CharField(max_length=255)
    sexe = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telephone = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=100)
    ville = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    usern = models.CharField(max_length=255)
    message_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Activation(models.Model):
    date_deactivated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    usersN = models.ForeignKey('recrues.UsersN', on_delete=models.CASCADE, related_name='activation')

    def __str__(self):
        return self.date_deactivated


def uploadFile(instance, filename):
    extension = filename.split('.')[-1]
    return 'static/uploadfile/recrues/{}.{}'.format(uuid4().hex, extension)

class NewRecrue(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='image')
    diplome = models.CharField(max_length=255)
    message = models.TextField()

    

    def __str__(self):
        return self.user.username


class NewRecrueRegister(models.Model):
    CHOICE = (
        ('partiel', 'Temps partiel'),
        ('Plein', 'Temps plein'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='image')
    diplome = models.CharField(max_length=50, choices=CHOICE)
    message = models.TextField()

    

    def __str__(self):
        return self.user.username

class NewRecrueRegister2(models.Model):
    CHOICE = (
        ('partiel', 'Temps Partiel'),
        ('Plein', 'Temps Plein'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='image')
    cv = models.FileField(verbose_name='upload your CV')
    diplome = models.CharField(max_length=50, choices=CHOICE)
    message = models.TextField()

    

    def __str__(self):
        return self.user.username

class NewRecrueRegistration(models.Model):
    CHOICE = (
        ('temps partiel', 'Temps Partiel'),
        ('temps Plein', 'Temps Plein'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='Telecharger votre image')
    cv = models.FileField(verbose_name='Telecharger votre CV')
    telephone = models.IntegerField()
    mode = models.CharField(max_length=50, choices=CHOICE)
    register_date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    

    def __str__(self):
        return self.user.username
