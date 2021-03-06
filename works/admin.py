from django.contrib import admin
from .models import Work, Content, Review


class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'name',
        'price',
        'is_sold',
        'image',
    )

    ordering = ('content',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'user_rating',
        'comment',
        'user',
        'created_on',
    )

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
admin.site.register(Review, ReviewAdmin)
