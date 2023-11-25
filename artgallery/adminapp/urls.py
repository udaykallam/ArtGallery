from django.urls import path
from. import views

urlpatterns = [
    path("adminhome/",views.adminhome,name="adminhome"),
    path('uploadopt/', views.upload_product, name='uploadopt'),
    path("adminlogout",views.logout,name="adminlogout"),
    path("feedbacks",views.feedbackpage,name="feedbacks"),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('delete_artist/', views.delete_artist, name='delete_artist'),
    path('orders',views.orders,name="orders"),
    path('requests',views.requests,name="requests"),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),

    ]
