from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        group = Group.objects.create(name='Product moderator')
        group.save()

        permission_publish = Permission.objects.get(codename='can_unpublish_product')
        remove_product = Permission.objects.get(codename='delete_product')
        group.permissions.add(permission_publish, remove_product)
        group.save()
