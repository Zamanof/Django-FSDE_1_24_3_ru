from django.urls import path
from .views import PingAPIView, DemoNotesAPIView

app_name = 'api'
urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='api-ping'),
    path("demo_notes/", DemoNotesAPIView.as_view(), name='demo-notes'),
]
