from django.urls import path
from . import views

urlpatterns = [
    path('drivers/register/', views.DriverCreateView.as_view(), name='drivers'),

    path('driver/me/', views.DriverMe.as_view()),
    path('user/me/', views.UserMe.as_view()),

    path('profile/published-ads/', views.PublishedAds.as_view(), name='published-ads'),
    path('cargo-types/', views.CargoTypes.as_view(), name='cargo-types'),

]
