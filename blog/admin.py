from django.contrib import admin
from .models import Blog,messageblog
# Register your models here.

admin.site.register(Blog)
class massageAdmin (admin.ModelAdmin):
    list_display =list_display=('full_name', 'email', 'message')
admin.site.register(messageblog,massageAdmin)
