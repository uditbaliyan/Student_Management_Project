from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest






class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None ,password=None ,  **kwargs) :

        UserModel=get_user_model()
        try:
            # comment: 
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        # end try
        else:
            # comment: 
            if (user.check_password(password)):
                # comment: 
                return user
            # end if
        return None

