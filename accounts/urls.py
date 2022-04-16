from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('comparatif', views.comparatif, name="comparatif"),
    path('mescomptes', views.mescomptes, name="mescomptes"),
    path('add_ca/', views.addCA, name="add_ca"),
    path('edit_ca/<str:pk>/', views.editCA, name="edit_ca"),
    path('delete_ca/<str:pk>/', views.deleteCA, name="delete_ca"),
    path('profile/', views.editProfile, name="profile"),
]
