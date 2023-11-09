from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustonUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

from .models import Produto, Recurso, Pacote

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustonUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name','email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso','ativo','modificado')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto','descricao','icone','ativo','modificado')

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sub_titulo', 'preco', 'display_recursos', 'ativo', 'modificado')

    def display_recursos(self, obj):
        return ", ".join([recurso.recurso for recurso in obj.recursos.all()])

    display_recursos.short_description = 'Recursos'

