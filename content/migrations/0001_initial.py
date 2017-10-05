# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContentTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='content.Content')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content.ContentTree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('enum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Enum')),
            ],
            bases=('content.enum',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('enum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Enum')),
            ],
            bases=('content.enum',),
        ),
        migrations.AddField(
            model_name='content',
            name='syllabus',
            field=models.ManyToManyField(related_name='contents', to='content.Syllabus'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabus', to='content.Standard'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabus', to='content.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='syllabus',
            unique_together=set([('subject', 'standard')]),
        ),
    ]
