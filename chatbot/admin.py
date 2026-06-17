from django.contrib import admin

from .models import (
    CMSContent,
    Programme,
    Syllabus,
    ChatHistory,
    Faculty,
    Event,
    Notice
)
admin.site.register(CMSContent)
admin.site.register(Programme)
admin.site.register(Syllabus)
admin.site.register(ChatHistory)
admin.site.register(Faculty)
admin.site.register(Event)
admin.site.register(Notice)
