from . import views 
from django.urls import path,include

app_name='survey'
urlpatterns = [
    path('', views.index, name='index'),
    # path('pdf/', views.generate_pdf, name='generate_pdf'),
]
