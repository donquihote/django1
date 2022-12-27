from distutils.command.upload import upload
from django.db import models
from traitlets import default

# Create your models here.
class Nganhnghe(models.Model):
    mangkinhdoanh=models.CharField(max_length=200, null=False)
    mota=models.TextField(null=True, blank=True)
    ngaytao=models.DateTimeField(auto_now_add=True)
    ngayupdate=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.mangkinhdoanh

class Chitiet(models.Model):
    mangkinhdoanh=models.CharField(max_length=200, null=False)
    mota=models.TextField(null=True, blank=True)
    hinhanh=models.ImageField(upload_to='hinhanh/%Y/%m')
    ngaytao=models.DateTimeField(auto_now_add=True)
    ngayupdate=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    slug=models.SlugField(unique=True, db_index=True, null=True)
    nganhnghe=models.ForeignKey(Nganhnghe, on_delete=models.CASCADE)