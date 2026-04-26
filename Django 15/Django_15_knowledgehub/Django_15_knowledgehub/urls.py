from django.contrib import admin
from django.urls import path, include

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("notes.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),

]