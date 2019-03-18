from restaurant_app.models import Person
from django.contrib.auth.models import User as AuthUser
from oauth2_provider.models import AccessToken


def check_user(request, user_id=None):
    access_header = request.META.get('HTTP_AUTHORIZATION').split()[1]
    access_token = AccessToken.objects.get(token=access_header)
    auth_user = AuthUser.objects.get(pk=access_token.user_id)

    if not Person.objects.filter(_auth_user_id=auth_user.id):
        return True, 'Cannot Access this User'

    db_person = Person.objects.get(_auth_user_id=auth_user.id)

    if not db_person.has_permission:
        if user_id and user_id != db_person.id:
            return True, 'The Token does not match with the User Id'

    return False, db_person
