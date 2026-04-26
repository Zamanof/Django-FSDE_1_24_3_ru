from django.http import HttpResponse, HttpRequest, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from .models import Note
from .forms import NoteForm

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "notes/home.html")

@login_required
def notes_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "notes/notes_list.html",
                  {"page_title": "Notes List", "notes": notes})

@login_required
def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if note.author != request.user:
        return HttpResponseForbidden("Ты типа такой хитрый что хочеш заметки других увидет? Ты хацкер?")
    return render(request, "notes/note_detail.html", {"note": note})

@login_required
def note_create(request: HttpRequest):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, "Note Created")
            return redirect("notes:note_detail", note_id=note.pk)
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form, "mode": "create"})

@login_required
def note_update(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)

    if note.author != request.user:
        return HttpResponseForbidden("Ты типа такой хитрый что хочеш заметки других изменить? Ты хаткер?")

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note Updated")
            return redirect("notes:note_detail", note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "mode":"edit", "note": note})
@login_required
def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)

    if note.author != request.user:
        return HttpResponseForbidden("Ты типа такой хитрый что хочеш заметки других изменить? Ты удалякер?")


    if request.method == "POST":
        note.delete()
        messages.success(request, "Note Deleted")
        return redirect("notes:notes_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})

@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("accounts:login")

def ping(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "pong"})