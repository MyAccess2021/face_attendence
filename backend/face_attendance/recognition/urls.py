from django.urls import path
from .views import *

urlpatterns = [
    path('api/get-face-embedding/', FaceEmbeddingFromImageFileView.as_view()),
    path('api/verify-face/', VerifyFaceAndMarkAttendance.as_view()),
]
