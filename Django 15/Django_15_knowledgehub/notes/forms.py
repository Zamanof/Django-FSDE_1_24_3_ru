from django import forms
from django.core.exceptions import ValidationError
from notes.models import Note


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows":4, "placeholder":"Write your Message"}),
        min_length=10,
    )

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "category", "tags"]
        labels = {
            "title": "Title",
            "content": "Content",
            "category": "Category",
            "tags": "Tags",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a clear, descriptive title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Write your note content here…",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "size": 8,
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if title.lower().startswith("test"):
            raise ValidationError("Title must start with test")
        return title