import constants

from django.db import models
from django.db.models import Q
from core.managers import TypeManager


class BaseProxy(models.Model):

    class Meta:
        abstract = True

    objects = TypeManager()

    @property
    def connections(self):
        return self._connections()

    def _connections(self):
        return EntityAffiliate.objects.filter(
            Q(entity_a=self) |
            Q(entity_b=self)
        )

    def connect(self, entity):
        try:
            from_self = Q(entity_a=self, entity_b=entity)
            to_self = Q(entity_b=self, entity_a=entity)
            aff = EntityAffiliate.objects.get(from_self | to_self)
        except EntityAffiliate.DoesNotExist:
            aff = EntityAffiliate.objects.create(entity_a=self, entity_b=entity)

        return aff

    def save(self, *args, **kwargs):
        self.type = int([v[0] for v in constants.ENTITY_TYPE if v[1] == self.__class__.__name__.lower()][0])
        super(BaseProxy, self).save(*args, **kwargs)


class Entity(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=constants.ENTITY_TYPE, default=0)
    affiliates = models.ManyToManyField('self',
                                        related_name='affiliations+',
                                        symmetrical=False,
                                        through='EntityAffiliate')
    metadata = models.ManyToManyField('MetaData')

    @property
    def name_parts(self):
        return self.name.split(' ')

    def __str__(self):
        return self.name


class EntityAffiliate(models.Model):
    entity_a = models.ForeignKey(Entity, related_name='from_entities')
    entity_b = models.ForeignKey(Entity, related_name='to_entities')
    tie_strength = models.IntegerField(default=1)

    def __str__(self):
        return '{0} - {1}'.format(self.entity_a, self.entity_b)


class MetaKey(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MetaData(models.Model):
    name = models.ForeignKey(MetaKey)
    val = models.IntegerField(db_index=True)

    @property
    def value(self):
        try:
            attr = getattr(constants, self.name.upper())
            return attr[self.val][1]
        except AttributeError:
            return self.val

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.value)


class Person(BaseProxy, Entity):

    class Meta:
        proxy = True

    @property
    def first_name(self):
        return self.name_parts[0]

    @first_name.setter
    def first_name(self, value):
        self.name = value

    @property
    def last_name(self):
        return ' '.join(self.name_parts[1:])

    @last_name.setter
    def last_name(self, value):
        self.name += ' {0}'.format(value)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Organization(BaseProxy, Entity):

    class Meta:
        proxy = True

    def __str__(self):
        return self.name