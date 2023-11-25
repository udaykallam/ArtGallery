from django.conf.urls.static import static
from django.urls import path
from. import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
     path("contact/",views.contactfunction,name="contactfunction"),
     path("greeitng",views.greeting,name="greeting"),
     path('search/', views.search_view, name='search'),
     path('search1/', views.search_view1, name='search1'),
     path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     path('address/<str:title>/<str:price>/',views.address,name="address"),
     path('message',views.message,name="message"),
     path('paymentpage/<str:title>/<str:price>/', views.paymentpage, name='paymentpage')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
