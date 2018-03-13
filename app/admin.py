from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from app.models import Channel, Playlist, Upload


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'group', 'playlist', 'created_at']
    search_fields = ['title', 'group', 'path']
    list_filter = ['created_at', 'playlist', ]
    ordering = ['-created_at']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'public_key', 'public_link', ]
    list_display = ['user', 'count', 'created_at']


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['info', 'user', 'created_at']


class EnhancedUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_joined', )
    ordering = ('-date_joined', )


admin.site.unregister(User)
admin.site.register(User, EnhancedUserAdmin)
