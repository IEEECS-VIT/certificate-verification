
from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/<int:id>', views.generate_certificate, name="generate_certificate"),
    path('display_certificate/<int:id>', views.display_certificate, name="display_certificate"),
    path('convert_to_pdf/<int:id>', views.convert_certificate_to_pdf, name="convert_certificate_to_pdf")
]