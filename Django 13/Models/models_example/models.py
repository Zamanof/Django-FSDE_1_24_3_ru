from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

'''
CharField - Короткая строка
TextField
IntegerField
BooleanField
DecimalField
DateField
TimeField
DateTimeField
ForeignKey
ManyToManyField
'''

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.EmailField(blank=True)

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Comments(models.Model):
    content = models.TextField()
    parent = (
        models.ForeignKey('self',
                          on_delete=models.SET_NULL,
                          related_name='children',
                          null=True,
                          blank=True
                          ))
    tags = models.ManyToManyField(Tags, related_name='comments')

# qs = Comments.objects.all()
# subset = qs.filter(status='published')
# data = subset.get(pk=1)

# CRUD
# note = Notes.objects.create(title="",  content="")
# note.save()
#
# one = Notes.objects.get(pk=note.pk)
# one.title = "one"
# one.save()
#
# one.delete()


