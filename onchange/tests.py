from django.test import TestCase

from onchange.models import Item, Status


class ItemTestCase(TestCase):
    def test_refresh_from_db(self):
        draft = Status.objects.create(name='draft')
        closed = Status.objects.create(name='closed')

        item = Item.objects.create(status=draft)
        Item.objects.filter(id=item.id).update(status=closed)
        item.refresh_from_db(fields=('status',))
