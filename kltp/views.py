from django.http import HttpResponse
from django.shortcuts import render
from .models import Chitiet,Nganhnghe

# Create your views here.


def index(request):
    return render(request, 'kltp/trangchu.html')

def tuvan(request):
    return render(request,'kltp/tuvantk.html')
       
def chothue(request):
    chitiet=Chitiet.objects.all()
    return render(request, 'kltp/chothue.html',{
        'ten': chitiet        
    })
        
def dongia(request):
    return render(request, 'kltp/dongia.html')
def lienhe(request):
    return render(request, 'kltp/lienhe.html')
def chitiet(request,chitiet_slug):
    chitiet=Chitiet.objects.get(slug=chitiet_slug)
    return render(request,'kltp/chitiet.html',{
        'hinh':chitiet.mangkinhdoanh,
        'mota':chitiet.mota,
        'anh':chitiet.hinhanh.url
    })
       