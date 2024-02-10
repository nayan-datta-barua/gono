from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.

# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Mode
class sidecontent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title
    
    
class Dailynews(models.Model):
    news_id = models.AutoField(primary_key=True,)
    title = models.CharField(max_length=200)
    content = models.TextField()
    cat = models.ForeignKey(Category,on_delete= models.CASCADE)
    image =models.ImageField(upload_to='dailynews/')
    date_uploaded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
class Weeklynews(models.Model):
    week_id=models.AutoField(primary_key=True,)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    image =models.ImageField(upload_to='weeknews/')
    date_uploaded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
class newnewsforegin(models.Model):
    new_id=models.AutoField(primary_key=True,)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    image =models.ImageField(upload_to='newnews/')
    date_uploaded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class vedio(models.Model):
    title= models.CharField(max_length=200)
    video = models.FileField(upload_to='videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)

class politics(models.Model):
    title= models.CharField(max_length=200)
    video = models.FileField(upload_to='videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)

