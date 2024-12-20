from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Adicionando um campo personalizado
    full_name = models.CharField(
        max_length=255, verbose_name=_("Full Name"), blank=True, null=True
    )

    def __str__(self):
        return self.full_name or self.username


class ActionLog(models.Model):
    # Usuário que realizou a ação
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_logs",
        verbose_name=_("User"),
    )
    # Texto descrevendo a ação
    action_text = models.TextField(verbose_name=_("Action Text"))
    # Data e hora da ação
    action_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Action Date"))

    def __str__(self):
        user_info = self.user.username if self.user else "Usuário Desconhecido"
        return f"Ação por {user_info}: {self.action_text}"
