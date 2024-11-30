from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name='homee' ),
    path('post/<int:pk>', post, name='postt' ),
    path('posts/', posts, name='postss' ),
    path('port/', port, name='portt' ),
    path('create/', create, name='cree'),
    path('test/', test, name='test'),
    path('update/<int:pk>', up, name='upp'),
    path('send_email', send_email, name='send_email'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )


# https://www.youtube.com/watch?v=iQcJPeCcjNo&list=PL-51WBLyFTg38qZ0KHkJj-paDQAAu9HiP&index=12&ab_channel=DennisIvy
# https://chatgpt.com/c/674aa662-7080-8003-9b40-be7c3154c902
# https://github.com/divanov11/django-portfolio-website/blob/master/base/models.py