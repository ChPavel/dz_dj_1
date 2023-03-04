from rest_framework.permissions import BasePermission

from users.models import UserRole


""" Проверка владельца подборки на соответствие запрашивающему пользователю"""

class IsOwnerSelection(BasePermission):
    message = "Вы не являетесь владельцем данной подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


""" Проверка владельца объявления на соответствие пользователю, запрашивающему удаление или изменение """

class IsOwnerAdOrStaff(BasePermission):
    message = "Вы не являетесь владельцем объявления или админом"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author_id or request.user.role in [UserRole.ADMIN, UserRole.MODERATOR]:
            return True
        return False