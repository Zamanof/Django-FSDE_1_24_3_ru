import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_15_knowledgehub.settings')
django.setup()

from api.serializers import NoteSerializer

serializer = NoteSerializer(data={
    "title": "Drf note",
    "content": "Django Rest Framework note",
})

serializer.is_valid()
print(serializer.errors)