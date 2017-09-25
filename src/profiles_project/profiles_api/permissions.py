from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profile.
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if a user is trying to edit his own profile.
        """

        # can view but cannot edit
        if request.method in permissions.SAFE_METHODS:
            return True

        # the obj profile id matches logged in user id
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status.
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if a user is trying to update his own status.
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
