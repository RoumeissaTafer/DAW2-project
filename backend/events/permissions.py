from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrganizerOrAdminOrReadOnly(BasePermission):
    """
    - SAFE methods (GET, HEAD, OPTIONS): allowed for everyone
    - Write methods: allowed only for:
        * authenticated user
        * with role 'ORGANIZER' or superuser
        * and (for object-level) must be admin of that event or superuser
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return getattr(user, "role", None) == "ORGANIZER"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        # only the admin of the event can update/delete it
        return getattr(obj, "admin", None) == user
