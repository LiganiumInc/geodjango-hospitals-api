# Generated by Django 4.2.7 on 2023-11-16 09:26

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("valhko_app", "0002_adm2_adm3_adm4"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="adm0",
            options={"verbose_name": "Country"},
        ),
        migrations.AddField(
            model_name="adm0",
            name="climate_finance",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm0",
            name="finance_all",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm1",
            name="climate_finance",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm1",
            name="finance_all",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm2",
            name="climate_finance",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm2",
            name="finance_all",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm3",
            name="climate_finance",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm3",
            name="finance_all",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm4",
            name="climate_finance",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
        migrations.AddField(
            model_name="adm4",
            name="finance_all",
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
    ]