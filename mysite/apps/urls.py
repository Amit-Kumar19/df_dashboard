from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello,name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logoutUser,name='logout'),
    path('preview/<pk>',views.geeks_view, name='preview-page')

]