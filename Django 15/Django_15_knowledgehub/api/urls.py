from django.urls import path, include
from .views import PingAPIView, DemoNotesAPIView, CategoryViewSet, TagViewSet, NotesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NotesViewSet, basename='notes')
router.register('categories', CategoryViewSet, basename='categories')
router.register('tags', TagViewSet, basename='tags')

app_name = 'api'
urlpatterns = [
    # path('ping/', PingAPIView.as_view(), name='api-ping'),
    # path("demo_notes/", DemoNotesAPIView.as_view(), name='demo-notes'),
    path("", include(router.urls)),
]
