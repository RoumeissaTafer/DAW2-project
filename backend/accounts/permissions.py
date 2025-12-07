from rest_framework.permissions import BasePermission


class IsOrganizer(BasePermission):
    """
    Allow access only to authenticated users with role ORGANIZER.
    """

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) == "ORGANIZER"
        )


class IsReviewer(BasePermission):
    """
    Allow access only to users with role REVIEWER (COMMITTEE).
    """

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) == "REVIEWER"
        )


class IsOrganizerOrAdmin(BasePermission):
    """
    Allow access to:
    - Django superuser (platform owner)
    - OR users whose role is ORGANIZER
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return getattr(user, "role", None) == "ORGANIZER"
