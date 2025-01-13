from django.contrib import admin
from .models import Group, Album, Song, GroupMember

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'release_date')
    search_fields = ('name', 'group__name')
    list_filter = ('release_date', 'group')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'group', 'duration')
    search_fields = ('name', 'album__name', 'group__name')
    list_filter = ('album', 'group')

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'instrument', 'group')
    search_fields = ('name', 'group__name')
    list_filter = ('group',)

