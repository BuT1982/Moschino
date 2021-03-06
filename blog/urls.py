from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("post/<slug:slug>/", GetPost.as_view(), name='post'),
    path("category/<slug:slug>/", PostsByCategory.as_view(), name='category'),
    path("about/", about, name='about'),
]