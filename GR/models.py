from django.db import models
from django.utils import timezone
# Create your models here.

class Intervention(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    text = models.CharField(max_length=500)
    style = models.IntegerField(default='1')
    link = models.CharField(max_length=500, default="")
    divclass = models.CharField(max_length=500, default="")
    displayorder = models.IntegerField(default='1')
    def __str__(self):
        return self.title

class Favorite(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    date_created = models.DateTimeField(blank=False, null=False)
    fav = models.ForeignKey(Intervention,on_delete=models.PROTECT)
    toggle=models.BooleanField(default="False")

    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        super(Favorite, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.author)
