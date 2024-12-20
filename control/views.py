from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = (
        "accounts/login/"  # URL para redirecionar caso o usuário não esteja logado
    )
    redirect_field_name = "next"  # Campo para armazenar a URL original
