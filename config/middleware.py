from social_django.middleware import SocialAuthExceptionMiddleware
from urllib.parse import quote


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        # 以下に基づき実装
        # DEBUG=Trueの時に動作しなくなるので注意
        # https://python-social-auth.readthedocs.io/en/latest/configuration/django.html?highlight=error#exceptions-middleware

        error_message = f"{type(exception).__name__}: {exception}"

        return f"/?error_message={quote(error_message)}"
