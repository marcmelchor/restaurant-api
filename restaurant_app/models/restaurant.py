from django.db import models
from restaurant_app.models import Person, RestaurantType
from filer.fields.image import FilerImageField


class Restaurant(models.Model):
    _user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    _title = models.CharField(max_length=100, blank=True, default='')
    _description = models.CharField(max_length=250)
    _phone = models.CharField(max_length=20, blank=True, default='')
    _type = models.IntegerField(choices=[(tag.value, tag) for tag in RestaurantType])
    _media = FilerImageField(related_name="restaurant_media", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self._title

    def __unicode__(self):
        return '/%s/' % self._title

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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
