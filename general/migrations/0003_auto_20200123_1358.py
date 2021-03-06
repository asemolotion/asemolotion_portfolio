# Generated by Django 2.2.9 on 2020-01-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20200120_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='タグ名')),
                ('slug', models.SlugField(unique=True, verbose_name='タグスラグ')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='general.Tag'),
        ),
    ]
