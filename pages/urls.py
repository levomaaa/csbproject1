from django.urls import path  
from .views import login_view, logout_view, profile_view  

urlpatterns = [  
    path('', login_view, name='index'),  
    path('logout/', logout_view, name='logout'),  
    path('profile/<str:username>/', profile_view, name='profile'),
]