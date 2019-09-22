from django.core.management import BaseCommand

from webapp.models import Employee, Equipment, Operation


class Command(BaseCommand):
    help = 'Fill DB with sample data'

    def handle(self, *args, **options):
        for obj in [Employee, Equipment, Operation]:
            obj.objects.all().delete()

        Employee.objects.create(name='Иван Петрович', number='8 808 0303030', title='CEO')
        Employee.objects.create(name='Пётр Иванович', number='8 808 1005000', title='CFO')
        Employee.objects.create(name='Гарик', number='8 900 0303030', title='охранник')

        Equipment.objects.create(name='Станок с ЧПУ', amount=3)
        Equipment.objects.create(name='Станок без ЧПУ', amount=8)
        Equipment.objects.create(name='ЧПУ без станка', amount=5)
        Equipment.objects.create(name='Ничего', amount=0)

        Operation.objects.create(title='Ничегонеделанье', number=1)
        Operation.objects.create(title='Ничегонеделанье', number=2)
        Operation.objects.create(title='Ничегонеделанье', number=3)


