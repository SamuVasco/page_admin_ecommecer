from .models import ActionLog


class LoggableMixin:
    """
    Mixin genérico para registrar logs automaticamente durante o save().
    """

    def save(self, *args, user=None, action_text=None, **kwargs):
        """
        Sobrescreve o método save para registrar logs de alterações.
        :param user: Instância do usuário que realizou a ação.
        :param action_text: Descrição da ação realizada.
        """
        # Chama o método save padrão para salvar o modelo
        super().save(*args, **kwargs)

        # Registrar o log
        if user and action_text:
            ActionLog.objects.create(
                user=user,
                employee=getattr(self, "employee", None),
                action_text=f"{action_text} - [{self.__class__.__name__}]",
            )
