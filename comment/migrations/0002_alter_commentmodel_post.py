# Generated by Django 4.0.5 on 2022-06-18 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_treadmodel_receiver_remove_treadmodel_user_and_more'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post'),
        ),
    ]