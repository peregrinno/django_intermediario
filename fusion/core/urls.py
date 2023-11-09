from django.urls import path
from .views import IndexView, https400View, https500View
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('404/', https400View.as_view(), name='404'),
    path('500/', https500View.as_view(), name='500'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
]