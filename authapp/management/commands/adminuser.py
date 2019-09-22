from django.core.management import BaseCommand

from authapp.models import WebUser
from simpleweb.settings import CONFIG


class Command(BaseCommand):
    help = 'Create super user'

    def handle(self, *args, **options):
        # superuser
        _superuser = WebUser.objects.filter(is_superuser=True).first()
        if not _superuser:
            WebUser.objects.create_superuser(
                username=CONFIG.get('SUPERUSER_NAME', 'django'),
                password=CONFIG.get('SUPERUSER_WORD', 'django'),
                email=CONFIG.get('SUPERUSER_MAIL', 'example@example.com')
            )
        else:
            print('super user exists: %s' % (_superuser.username, ))
