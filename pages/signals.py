from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    users = [
        ("kalle", "1234"),
        ("pirkka", "0000"),
    ]
    
    for username, password in users:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)