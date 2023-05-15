from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorPermission(BasePermission):
    """Только автор может изменять объекты"""

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or obj.author == request.user)
