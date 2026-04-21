from django.urls import path


from .views import (
    home,
    note_create,
    note_detail,
    notes_list,
    note_update,
    note_delete,
    logout_view,

)

app_name = 'notes'
urlpatterns = [
    path("", home, name="home"),
    path("notes", notes_list, name="notes_list"),
    path("notes/<int:note_id>/", note_detail, name="note_detail"),
    path("notes/create/", note_create, name="note_create"),
    path("notes/<int:note_id>/edit", note_update, name="note_update"),
    path("notes/<int:note_id>/delete", note_delete, name="note_delete"),
    path("logout/", logout_view, name="logout"),

]