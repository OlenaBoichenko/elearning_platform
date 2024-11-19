from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver

        @receiver(post_migrate)
        def create_groups(sender, **kwargs):
            if sender.name == 'courses':
                Group.objects.get_or_create(name='Teachers')
                Group.objects.get_or_create(name='Students')

        post_migrate.connect(create_groups, sender=self)
