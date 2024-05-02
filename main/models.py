from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):
    company_name= models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    extra_phone = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Banner(models.Model):
    photo = models.ImageField(upload_to='Banner/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Ad(models.Model):
    photo = models.ImageField(upload_to='Banner/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)    
    is_full = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=255)

class ProductPhoto(  models.Model):
    photo = models.ImageField(upload_to='ProductPhoto/')

class ProductInfo(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ManyToManyField(ProductPhoto)
    rating = models.IntegerField()
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    info_more = models.ManyToManyField(ProductInfo)
    in_ad = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

class Partners(models.Model):
    photo = models.ImageField(upload_to='partner/')



class Blog(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/')
    date = models.DateField()
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)



class Service(models.Model):
    photo = models.ImageField(upload_to='service/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)    


class Email(models.Model):
    email = models.CharField(max_length=255)



class Video(models.Model):
    bg_photo =models.ImageField(upload_to='video/')  
    video = models.CharField(max_length=255)



class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)    




class Team(models.Model):
    photo =models.ImageField(upload_to='team/')  
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)




class Testimonial(models.Model):
    photo =models.ImageField(upload_to='testimonial/')  
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    text = models.CharField(max_length=255)    
    rating = models.IntegerField()




class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


 
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255) 


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)