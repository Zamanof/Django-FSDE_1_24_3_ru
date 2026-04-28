from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions

from api.permissions import IsAuthorOrReadOnly
from api.serializers import NoteSerializer, CategorySerializer, TagSerializer
from notes.models import Note, Category, Tag


# Create your views here.
class PingAPIView(APIView):
    def get(self, request):
        return Response({'message': 'pong'})

class DemoNotesAPIView(APIView):
    notes = [
        {
            "id":1,
            "title":"first note",
            "status" : "published"
        }
    ]
    def get(self, request):
        return Response({'notes': self.notes}, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data
        next_id = len(self.notes)+1
        note = {
            "id":next_id,
            "title":payload.get("title", "Some title"),
            "status":payload.get("status", "draft"),
        }
        self.notes.append(note)
        return Response(note, status=status.HTTP_201_CREATED)

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.select_related("author", "category").prefetch_related("tags")
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]