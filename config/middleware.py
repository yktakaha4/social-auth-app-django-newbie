from social_django.middleware import SocialAuthExceptionMiddleware
from urllib.parse import quote


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        error_message = f"{type(exception).__name__}: {exception}"

        return f"/?error_message={quote(error_message)}"
