# Generated by Django 4.2.3 on 2023-07-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('type_p', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
