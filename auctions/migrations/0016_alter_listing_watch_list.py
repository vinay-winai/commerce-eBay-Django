# Generated by Django 4.1 on 2022-10-03 05:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0015_remove_listing_price_bid_item_listing_curr_bid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="watch_list",
            field=models.ManyToManyField(
                blank=True, related_name="user", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]