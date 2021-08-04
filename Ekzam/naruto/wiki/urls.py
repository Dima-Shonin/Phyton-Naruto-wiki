from django.urls import path
from  . import views
app_name = 'wiki'

urlpatterns = [
    path('',views.index , name='index'),
    path('Villages',views.Villages , name='Villages'),
    path('Village/<int:pk>/',views.Village_detail , name='Village_detail'),
    path('Shinobies',views.Shinobies , name='Shinobies'),
    path('Shinobi/<int:pk>/',views.Shinobi_detail , name='Shinobi_detail'),
    path('Technics',views.Technicss , name='Technics'),
    path('Technic/<int:pk>/',views.Technic_detail , name='Technic_detail'),
    path('Battles',views.Battles , name='Battles'),
    path('Battle/<int:pk>/',views.Battle_detail , name='Battle_detail'),
    path('api/shinobi/all',views.ShinobiListAPIView.as_view(),name = "api-shinobi-list")
]