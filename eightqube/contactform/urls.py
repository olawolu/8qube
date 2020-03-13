from django.urls import path, include

from .views import ContactFormView, SingleMessageView

app_name = "contactform"

urlpatterns = [
    path('message', ContactFormView.as_view()),
    path('message/<init:pk>', SingleMessageView.as_view()),
]
