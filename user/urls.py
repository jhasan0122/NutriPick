from django.urls import path
from .views import CustomLoginView,register,profile_update_view

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',register,name='register'),
    path('profile/', profile_update_view, name='profile'),

]