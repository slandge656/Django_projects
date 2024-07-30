from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .  import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('signup/',views.User_Signup,name='signup'),
    path('login/',views.User_Login,name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)