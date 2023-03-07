from django.urls import path
#from .views import UserList, UserDetail, UsertypeList, UsertypeDetail, MaterielList, MaterielDetail
from . import views
urlpatterns = [
    path('usertype/get', views.getAll, name="get"),
    path('usertype/add/', views.add, name="add"),
    path('usertype/update/<int:pk>/', views.update, name="update"),
    path('usertype/delete/<int:pk>/', views.delete, name="delete"),
    path('materiel/addmat/', views.addmat, name="addmat"),
]