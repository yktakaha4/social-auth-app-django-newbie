from social_django.middleware import SocialAuthExceptionMiddleware
from social_core.exceptions import AuthCanceled
from urllib.parse import quote


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        # 以下に基づき実装
        # DEBUG=Trueの時に動作しなくなるので注意
        # https://python-social-auth.readthedocs.io/en/latest/configuration/django.html?highlight=error#exceptions-middleware
        REDIRECT_URL = "/"

        if isinstance(exception, AuthCanceled):
            # キャンセルはエラーではないのでメッセージは表示しない
            print("detect AuthCanceled.")
            error_message = None
        else:
            error_message = f"{type(exception).__name__}: {exception}"

        if error_message:
            return f"{REDIRECT_URL}?error_message={quote(error_message)}"
        else:
            return REDIRECT_URL
