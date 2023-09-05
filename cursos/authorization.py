from rest_framework import permissions

# importando da classe PERMISSION


class SuperUser(permissions.BasePermission):

    # modificando o metodo de permissao
    def has_permission(self, request, view):
        # se o metodo for DELETE, apenas o super usuario pode
        if request.method == "DELETE":
            if request.user.is_superuser:
                return True
            return False
        return True
