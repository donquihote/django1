from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='trangchu'),
    path('tu-van', views.tuvan, name= "tuvan"),
    path('cho-thue', views.chothue, name= 'chothue'),
    path('don-gia', views.dongia, name= 'dongia'),
    path('lien-he', views.lienhe, name= 'lienhe'),
    path('<slug:chitiet_slug>', views.chitiet, name= 'chitiet')
]
