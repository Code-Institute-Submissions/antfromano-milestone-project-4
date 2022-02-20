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
    )

    ordering = ('work',)

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
admin.site.register(Review, ReviewAdmin)
