import json

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.internal.models import User


class Principal(BaseAuthentication):
    """
    Base Auth class
    """
    def authenticate(self, request):
        """
        Authentication function
        """
        principal = self.get_header(request)
        try:
            user = User.objects.get(pk=principal['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found for this principal')

        return user, None

    @staticmethod
    def get_header(request) -> str:
        """
        Extracts the header containing the X-Principal
        request.
        """
        principal_header = request.headers.get('X-Principal')

        if not principal_header:
            raise AuthenticationFailed('No X-Principal header found')

        return json.loads(principal_header)
