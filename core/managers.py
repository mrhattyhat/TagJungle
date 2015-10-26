from django.db import models
from constants import ENTITY_TYPE


class TypeManager(models.Manager):

    def get_queryset(self):
        entity_type = int([v[0] for v in ENTITY_TYPE if v[1] == self.model.__name__.lower()][0])
        return super(TypeManager, self).get_queryset().filter(type=entity_type)
