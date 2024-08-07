from django.contrib.auth.backends import ModelBackend
from user.models import Member


class AuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Member.objects.get(email=email)
            if user.check_password(password):
                return user
        except Member.DoesNotExist:
            return None
        return None
