from django.contrib import admin
from .models import Project
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields=('created',)

admin.site.register(Project)
admin.site.register(Todo, TodoAdmin)
