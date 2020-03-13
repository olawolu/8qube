from django.urls import path, include

from .views import ContactFormView

app_name = "contactform"

urlpatterns = [
    path('message', ContactFormView.as_view()),
]