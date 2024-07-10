from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('train_search/', views.train_search, name='train_search'),
    path('train_result/', views.train_result, name='train_result'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-train/', views.add_train, name='add_train'),
    path('delete-train/<int:train_id>/', views.delete_train, name='delete_train'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
