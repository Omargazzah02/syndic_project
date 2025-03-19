# urls.py de ton app
from django.urls import path
from .views import UserPropretiesListAPIView

urlpatterns = [
 path('my-properties/', UserPropretiesListAPIView.as_view(), name='user-properties'),]
