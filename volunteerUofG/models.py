
from django.db import models
from django.contrib.auth.models import User





class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, default="")           
    interested_in = models.CharField(max_length= 350, default='')
    availability = models.CharField(max_length= 350, default='')
    introduce_yourself = models.TextField(max_length=500,default='')
    image = models.ImageField(upload_to='images/',default='https://cdn3.vectorstock.com/i/1000x1000/30/97/flat-business-man-user-profile-avatar-icon-vector-4333097.jpg')
    profile_picture = models.ImageField(null=True, blank=True)
    def __str__(self):
    	return self.user.username


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,default="")
    address = models.CharField(max_length= 350,default='')
    phone = models.CharField(max_length=12,default='')
    website = models.URLField(max_length=200,default='')
    description = models.TextField(max_length=500,default='')
    image = models.ImageField(upload_to='images/', default='https://m.media-amazon.com/images/I/4193V9-69jS._AC_SY780_.jpg')
    profile_picture = models.ImageField(null=True, blank=True)
    
    def __str__(self):
    	return self.user.username

class Opportunity(models.Model):
    title = models.CharField(max_length= 50, blank = False)
    creator = models.ForeignKey(Charity, on_delete=models.CASCADE)
    url = models.CharField(max_length=60)
    description = models.TextField(max_length=500,default='')
    skills = models.TextField(max_length=500,default='')
    location = models.CharField(max_length= 350,default='')
    time = models.CharField(max_length= 350, default='')
    image = models.ImageField(upload_to='images/',default='https://www.covenantgroup.com/img/84')
    profile_picture = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
