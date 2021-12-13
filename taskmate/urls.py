from django.contrib import admin
from django.urls import path
from django.urls import include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/',include("todolist.urls")),
    path('account/',include("user_app.urls")),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
]
