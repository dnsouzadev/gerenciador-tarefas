from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_task, name='list_task'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('detail/<int:id>/', views.detail_task, name='detail_task'),
]
