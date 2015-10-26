# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(default=0, choices=[(0, b'unknown'), (1, b'person'), (2, b'organization'), (3, b'location'), (4, b'publication')])),
            ],
        ),
        migrations.CreateModel(
            name='EntityAffiliate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tie_strength', models.IntegerField(default=1)),
                ('entity_a', models.ForeignKey(related_name='from_entities', to='core.Entity')),
                ('entity_b', models.ForeignKey(related_name='to_entities', to='core.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='metadata',
            name='name',
            field=models.ForeignKey(to='core.MetaKey'),
        ),
        migrations.AddField(
            model_name='entity',
            name='affiliates',
            field=models.ManyToManyField(related_name='affiliations+', through='core.EntityAffiliate', to='core.Entity'),
        ),
        migrations.AddField(
            model_name='entity',
            name='metadata',
            field=models.ManyToManyField(to='core.MetaData'),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('core.entity', models.Model),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('core.entity', models.Model),
        ),
    ]
