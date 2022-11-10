# Generated by Django 4.1 on 2022-09-28 18:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0009_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="bid", name="item",),
        migrations.RemoveField(model_name="listing", name="base_bid",),
        migrations.AddField(
            model_name="listing",
            name="curr_bid",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="auctions.bid",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="bid",
            name="new_bid",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(99999999.99),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="img",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name="user", name="email", field=models.EmailField(max_length=64),
        ),
    ]
