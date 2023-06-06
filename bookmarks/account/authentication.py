from django.contrib.auth.models import User

class EmailAuthBackend:
    """Аутентификация с помощью электронной почты"""
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

        def get_user(user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None
