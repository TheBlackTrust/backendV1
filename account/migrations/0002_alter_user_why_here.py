# Generated by Django 4.2.3 on 2023-09-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='why_here',
            field=models.CharField(choices=[('search engine', 'Search engine'), ('social media', 'Social media'), ('website referral', 'Website referral'), ('radio/tv', 'Radio/TV'), ('twitter space', 'Twitter space'), ('podcast', 'Podcast'), ('print', 'Print'), ('word of mouth', 'Word of Mouth'), ('others', 'Others')], max_length=400),
        ),
    ]