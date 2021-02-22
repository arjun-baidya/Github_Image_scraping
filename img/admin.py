from django.contrib import admin
from .models import Github


# Register your models here.
class githubadmin(admin.ModelAdmin):
    list_display = ('githubuser', 'imagelink', 'username')
    list_filter = ('username',)
    search_fields = ['githubuser']


admin.site.register(Github, githubadmin)
