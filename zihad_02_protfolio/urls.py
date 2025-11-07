
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from protfolio.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name='homePage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('addDetails/',addDetails,name='addDetails'),
    path('profilePage/',profilePage,name='profilePage'),
    path('update/',update,name='update'),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
