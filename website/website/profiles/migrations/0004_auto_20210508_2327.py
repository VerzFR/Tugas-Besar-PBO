# Generated by Django 3.2.2 on 2021-05-08 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_account_number_moneytransfer_account_number_transfer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='account_number_transfer',
            new_name='enter_the_amount_to_be_transferred_in_INR',
        ),
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='transfer',
            new_name='enter_the_destination_account_number',
        ),
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='your_username',
            new_name='enter_your_user_name',
        ),
    ]
