from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from User.models import User

UserModel = User


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email__iexact=email))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)  # This does nothing useful here.
            return None
        except UserModel.MultipleObjectsReturned:
            user = (
                UserModel.objects.filter(Q(email__iexact=email)).order_by("id").first()
            )

        if user is not None and user.check_password and user.is_active:
            return user
        return None


class ActiveAccountBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(phone_number=username)
            if (
                user.check_password(password)
                and self.user_can_authenticate(user)
                and user.is_active
            ):
                return user
        except User.DoesNotExist:
            return None


from User.models import User


# Phone number backends by Sabbir hossain
class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password) and user.is_active:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
