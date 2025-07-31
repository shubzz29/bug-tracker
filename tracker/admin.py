from django.contrib import admin
from .models import BugReport

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')