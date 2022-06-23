from django.urls import path

from web.views import index, detail, about

app_name = "web"
urlpatterns = [
    path('', index),
    path('detail/<int:pk>', detail),
]