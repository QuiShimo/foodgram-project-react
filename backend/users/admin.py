from django.contrib import admin

from users.models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email',)
    list_filter = ('first_name', 'last_name',)
    ordering = ('username', )
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = (
        'user__username', 'user__email', 'author__username', 'author__email'
    )


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
