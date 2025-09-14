from django.contrib import admin
from django.urls import path
from pages import views  # import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),     # home page
    path('about/', views.about, name='about'),  # about page
]
