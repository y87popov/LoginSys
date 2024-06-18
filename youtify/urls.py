from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
