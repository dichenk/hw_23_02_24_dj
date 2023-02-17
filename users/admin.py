from django.contrib import admin

from users.models import User

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'price', 'category',)
    search_fields = ('username', 'email',)
    list_filter = ('username',)
