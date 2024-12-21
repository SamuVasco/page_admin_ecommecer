# signals.py
from django.db.models.signals import post_migrate
from .models import User
from django.dispatch import receiver
from decouple import config


def create_default_user(sender, **kwargs):
    """
    Signal to create a default admin user when the database is created.
    """
    if User.objects.filter(username=config("DEFAULT_ADMIN_USERNAME", default="admin")).exists():
        return  # User already exists

    username = config("DEFAULT_ADMIN_USERNAME", default="admin")
    email = config("DEFAULT_ADMIN_EMAIL", default="admin@example.com")
    password = config("DEFAULT_ADMIN_PASSWORD", default="admin123")

    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")

post_migrate.connect(create_default_user)
    