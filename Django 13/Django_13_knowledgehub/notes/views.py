from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from notes import data


class AboutPageView(TemplateView):
    template_name = 'notes/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = "Knowledge Hub"
        context["author"] = "Nadir Zamanov"
        return context


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "notes/home.html")


# def about(request: HttpRequest) -> HttpResponse:
#     context = {
#         "project_name": "Knowledge Hub",
#         "author": "Nadir Zamanov",
#     }
#     return render(request, "notes/about.html", context)


def notes_list(request: HttpRequest) -> HttpResponse:
    return render(request, "notes/notes_list.html",
                  {"page_title": "Notes List", "notes": data.TEMP_NOTES})


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = next((item for item in data.TEMP_NOTES if item["id"] == note_id), None)
    return render(request, "notes/note_detail.html", {"note": note})