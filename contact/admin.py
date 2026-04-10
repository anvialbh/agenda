from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id', 'first_name', 'last_name',
    # list_filter = 'created_date', # para adicionar um filtro na lateral do admin
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name', # para permitir a edição direta no admin
    list_display_links = 'id', 'first_name', 'last_name', # para permitir clicar no id para editar o contato
    