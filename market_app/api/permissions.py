from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_staff = bool(request.user and request.user.is_staff)
        not_Kevin = request.user.username != "Kevin"
        # is_Laureen = request.user.username = "Laureen"
        print("not_Kevin", not_Kevin)
        return is_staff and not_Kevin or request.method in SAFE_METHODS
    
class IsAdminForDeleteOrPatchAndReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return bool(request.user and request.user.is_superuser)
        else: 
            return bool(request.user and request.user.is_staff)

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.user and request.user == obj.user)