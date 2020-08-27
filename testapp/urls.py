from django.contrib import admin
from django.urls import path , include
from testapp import views
urlpatterns = [
    path('',views.index_view,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]