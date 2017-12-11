from django.db import models
from polymorphic.models import PolymorphicModel


class Status(models.Model):
    name = models.CharField(max_length=128)


class Item(PolymorphicModel):
    status = models.ForeignKey('onchange.Status', on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.old_status_id = self.status_id
