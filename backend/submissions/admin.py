from django.contrib import admin
from .models import Submission
# Register your models here.
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'event', 'status', 'sub_date')
    list_filter = ('status', 'event')
    search_fields = ('title', 'author__username', 'event__title')
    readonly_fields = ('sub_date',)