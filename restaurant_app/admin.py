from django.contrib import admin
from .models import Person, Restaurant, Menu, Vote
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', '_first_name', '_email')
    search_fields = ('_email', '_first_name', '_last_name')

    def get_form(self, request, obj=None, change=False, **kwargs):
        self.exclude('_password')
        form = super(PersonAdmin, self).get_form(request, obj=None, **kwargs)
        return form


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', '_title')
    search_fields = ('_title', '_description', '_phone', '_type')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', '_title')
    search_fields = ('_title', '_description', '_date', '_restaurant')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', '_user')
    search_fields = ('_user', '_user_id', '_menu', '_menu_id')


admin.site.register(Person, PersonAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Vote, VoteAdmin)
