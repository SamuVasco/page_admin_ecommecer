from django.db.models.signals import post_migrate
from .models import Permission, Achievement


def create_permissions_and_achievements(sender, **kwargs):
    """
    Signal para criar permissões e conquistas padrão após a migração.
    """
    # Lista de permissões padrão
    predefined_permissions = [
        {'id': '1', 'name': 'Visualizar Relatórios'},
        {'id': '2', 'name': 'Gerenciar Usuários'},
        {'id': '3', 'name': 'Editar Configurações'},
        {'id': '4', 'name': 'Aprovar Solicitações'},
    ]

    # Lista de conquistas padrão
    predefined_achievements = [
        {'id': '1', 'name': 'Funcionário do Mês', 'image': 'achievements/employee_of_the_month.png'},
        {'id': '2', 'name': 'Meta Alcançada', 'image': 'achievements/goal_achieved.png'},
        {'id': '3', 'name': 'Aniversário de Empresa', 'image': 'achievements/company_anniversary.png'},
    ]

    # Criar permissões padrão, se não existirem
    for permission_data in predefined_permissions:
        permission, created = Permission.objects.get_or_create(
            id=permission_data['id'],
            defaults={'name': permission_data['name']}
        )
        if created:
            print(f"Permissão criada: {permission.name}")

    # Criar conquistas padrão, se não existirem
    for achievement_data in predefined_achievements:
        achievement, created = Achievement.objects.get_or_create(
            name=achievement_data['name'],
            defaults={'image': achievement_data['image']}
        )
        if created:
            print(f"Conquista criada: {achievement.name}")

post_migrate.connect(create_permissions_and_achievements)