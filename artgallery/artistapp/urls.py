from django.urls import path
from. import views

urlpatterns=[
    path('artisthome',views.artisthome,name="artisthome"),
    path('artistlogout',views.artistlogout,name="artistlogout"),
    path('artistupload',views.artistupload,name="artistupload"),
    path('artistabout',views.artistabout,name="artistabout"),
    path('request',views.requestpage,name="request"),
    path('artistaddress/<str:title>/<str:price>/',views.artistaddress,name="artistaddress"),
    path('artistpaymentpage/<str:title>/<str:price>/', views.artistpaymentpage, name='artistpaymentpage')
]
