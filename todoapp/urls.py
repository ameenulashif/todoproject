from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Tasklist.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Detail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Update.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Delete.as_view(),name='cbvdelete')
]
