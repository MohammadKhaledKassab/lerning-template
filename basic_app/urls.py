# -*- coding: utf-8 -*-
from django.urls import path
from .views import relativeView, otherView

# SET THE NAMESPACE!
# app_name = 'basic_app'

urlpatterns = [
    path('other/', otherView, name='other'),
    path('relative/', relativeView, name='relative'),
    
]