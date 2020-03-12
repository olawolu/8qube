from django.urls import path, include

from .views import ContactFormView

app_name = "contactform"

urlpatterns = [
    path('mails/', ContactFormView.as_view()),
]