# Generated by Django 4.2.7 on 2023-11-22 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ktalk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ktalk.themetest')),
            ],
        ),
    ]
