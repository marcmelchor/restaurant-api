from django.db import models
from django.contrib.auth.models import User as AuthUser
from restaurant_app.models import PersonGender, GroupOfAge


class Person(models.Model):
    _first_name = models.CharField(max_length=100, blank=True, default='')
    _last_name = models.CharField(max_length=100, blank=True, default='')
    _email = models.EmailField(max_length=100)
    _email_confirmed = models.BooleanField(default=False)
    _password = models.CharField(max_length=100)
    _birthday = models.DateField(null=True, blank=True, default=None)
    _gender = models.IntegerField(choices=[(tag.value, tag) for tag in PersonGender])
    _group_of_age = models.IntegerField(choices=[(tag.value, tag) for tag in GroupOfAge])
    _auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self._email

    def __unicode__(self):
        return '/%s/' % self._email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def email_confirmed(self):
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, value):
        self._email_confirmed = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def birthday(self):
        return None if self._birthday is None else int(self._birthday.timestamp())

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def group_of_age(self):
        return self._group_of_age

    @group_of_age.setter
    def group_of_age(self, value):
        self._group_of_age = value

    @property
    def auth_user(self):
        return self._auth_user

    @auth_user.setter
    def auth_user(self, value):
        self._auth_user = value

    @property
    def auth_user_id(self):
        return self._auth_user_id

    @auth_user_id.setter
    def auth_user_id(self, value):
        self._auth_user_id = value
