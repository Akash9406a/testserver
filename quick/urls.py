from django.urls import path
from . import views


urlpatterns = [
  path('login/',views.internalLoginView.as_view(),name='internallogin_page'),
]