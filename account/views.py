from django.views.generic import TemplateView

from social_django.models import UserSocialAuth

# Create your views here.
class AccountView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        user = request.user
        auth = (
            UserSocialAuth.objects.get(user_id=user.id)
            if user.is_authenticated
            else None
        )

        context = {"user": request.user, "auth": auth}

        return self.render_to_response(context=context)
