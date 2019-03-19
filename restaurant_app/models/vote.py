from django.db import models
from restaurant_app.models import Person, Menu


class Vote(models.Model):
    _user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    _menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    _created_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('_user', '_menu',)

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return '/%s/' % str(self.id)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, value):
        self._menu = value

    @property
    def menu_id(self):
        return self._menu_id

    @menu_id.setter
    def menu_id(self, value):
        self._menu_id = value

    @property
    def created_date(self):
        return int(self._created_date.timestamp())

    @created_date.setter
    def created_date(self, value):
        self._created_date = value
