# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('optimize.urls')),
# ]
from django.contrib import admin
from django.urls import path
from optimize import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
