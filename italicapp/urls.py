from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_document, name='upload'),
    path('download/<int:document_id>/', views.download_document, name='download_document'),
]