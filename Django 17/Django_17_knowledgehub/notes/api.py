from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Category, Note, Tag

class AuthenticatedWriteAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list

    def read_detail(self, object_list, bundle):
        return True

    def _is_authenticated(self, bundle):
        return bundle.request.user.is_authenticated

    def create_list(self, object_list, bundle):
        return object_list if self._is_authenticated(bundle) else []

    def create_detail(self, object_list, bundle):
        return self._is_authenticated(bundle)

    def update_list(self, object_list, bundle):
        return object_list if self._is_authenticated(bundle) else []

    def update_detail(self, object_list, bundle):
        return self._is_authenticated(bundle)

    def delete_list(self, object_list, bundle):
        return object_list if self._is_authenticated(bundle) else []

    def delete_detail(self, object_list, bundle):
        return self._is_authenticated(bundle)


class NoteOwnerAuthorization(Authorization):
    def update_detail(self, object_list, bundle):
        if not super().update_detail(object_list, bundle):
            return False
        return bundle.obj.author_id == bundle.request.user.id

    def delete_detail(self, object_list, bundle):
        if not super().delete_detail(object_list, bundle):
            return False
        return bundle.obj.author_id == bundle.request.user.id

    def update_list(self, object_list, bundle):
        if not bundle.request.user.is_authenticated:
            return object_list.none()
        return object_list.filter(author=bundle.request.user)

    def delete_list(self, object_list, bundle):
        if not bundle.request.user.is_authenticated:
            return object_list.none()
        return object_list.filter(author=bundle.request.user)


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get', 'post', "patch", "delete"]
        authorization = AuthenticatedWriteAuthorization()

        filtering = {"name": ["exact", "icontains"]}


class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tags'
        allowed_methods = ['get', 'post', "patch", "delete"]
        authorization = AuthenticatedWriteAuthorization()
        filtering = {"name": ["exact", "icontains"]}


class NoteResource(ModelResource):
    author_username = fields.CharField(attribute='author__username', readonly=True)

    class Meta:
        queryset = Note.objects.select_related('author', "category").prefetch_related("tags")
        resource_name = 'notes'
        allowed_methods = ['get', 'post', "patch", "delete"]
        authorization = NoteOwnerAuthorization()
        filtering = {
            "title": ["exact", "icontains"],
            "author": ["exact"],
            "category": ["exact"],
            "tag": ["exact"],
        }
        excludes = ["author"]

    def obj_create(self, bundle, **kwargs):
        return super().obj_create(bundle,author=bundle.request.user, **kwargs)

    def obj_update(self, bundle, **kwargs):
        kwargs["author"] = bundle.request.author
        return super().obj_update(bundle, **kwargs)







