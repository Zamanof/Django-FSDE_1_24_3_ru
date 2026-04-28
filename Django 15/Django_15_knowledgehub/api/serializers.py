from rest_framework import serializers
from notes.models import Note, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name",]

class NoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
        allow_null=True
    )
    tags_id = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        write_only=True,
        required=False,
        many=True,
    )

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "author",
            "category",
            "tags",
            "tags_id",
            "category_id",
            "created_at",
            "updated_at",]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def validate_title(self, attrs):
        if len(attrs.strip()) < 3:
            raise serializers.ValidationError("Title is too short. Must be at least 3 characters long")
        return attrs




