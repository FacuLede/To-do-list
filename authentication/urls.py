from django.urls import path
from authentication import views
from authentication.views import Signup

urlpatterns = [
    path('',views.home, name= "home"),
    path('signup/',Signup.as_view(), name= "signup"),    
    path('login/',views.log_in, name= "log_in"),   
    path('logout/',views.log_out, name= "log_out"),   
] 