# Generated by Django 4.1 on 2022-10-02 07:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0014_remove_bid_item_remove_listing_curr_bid_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="listing", name="price",),
        migrations.AddField(
            model_name="bid",
            name="item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="auctions.listing",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="curr_bid",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(99999999.99),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bid", name="new_bid", field=models.FloatField(),
        ),
    ]
