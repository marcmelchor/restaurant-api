from django.db import models
from restaurant_app.models import Person, Restaurant
from filer.fields.image import FilerImageField


class Menu(models.Model):
    _user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    _restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    _title = models.CharField(max_length=100, blank=True, default='')
    _description = models.CharField(max_length=250)
    _date = models.DateField(null=True, blank=True)
    _appetizer = models.CharField(max_length=100)
    _main_course = models.CharField(max_length=100)
    _dessert = models.CharField(max_length=100)
    _drink = models.CharField(max_length=100)
    _total_votes = models.IntegerField(default=0, blank=True, null=True)
    _media = FilerImageField(related_name="menu_media", null=True, blank=True, on_delete=models.SET_NULL)

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
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        self._restaurant = value

    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, value):
        self._restaurant_id = value

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
    def date(self):
        return None if self._date is None else int(self._date.timestamp())

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def appetizer(self):
        return self._appetizer

    @appetizer.setter
    def appetizer(self, value):
        self._appetizer = value

    @property
    def main_course(self):
        return self._main_course

    @main_course.setter
    def main_course(self, value):
        self._main_course = value

    @property
    def dessert(self):
        return self._dessert

    @dessert.setter
    def dessert(self, value):
        self._dessert = value

    @property
    def drink(self):
        return self._drink

    @drink.setter
    def drink(self, value):
        self._drink = value

    @property
    def total_votes(self):
        return self._total_votes

    @total_votes.setter
    def total_votes(self, value):
        self._total_votes = value

    @property
    def media(self):
        return self._media

    @media.setter
    def media(self, value):
        self._media = value
