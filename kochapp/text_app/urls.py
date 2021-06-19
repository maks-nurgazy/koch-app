from django.urls import path
from . import views


urlpatterns = [
    path('about-us/', views.AboutUsView.as_view()),
    path('privacy/', views.PrivacyView.as_view()),

]
