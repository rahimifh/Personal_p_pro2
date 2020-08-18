from django.contrib import admin
from .models import Project,course,lesson,LibFile,LibPartition,lesson_detail,messageservices
# Register your models here.

# Register your models here.
admin.site.register(course)
admin.site.register(lesson)
admin.site.register(Project)
admin.site.register(LibFile)
admin.site.register(LibPartition)
admin.site.register(lesson_detail)
class massageAdmin (admin.ModelAdmin):
    list_display =list_display=('full_name', 'email', 'message')

admin.site.register(messageservices,massageAdmin)
# Register your models here.
