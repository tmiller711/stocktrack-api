<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-11-07 03:09
=======
# Generated by Django 4.1.5 on 2023-01-15 00:40
>>>>>>> 68bccf09 (renames structure)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=30)),
<<<<<<< HEAD
                ('stock_data', models.FileField(upload_to='stocks')),
=======
                ('stock_data', models.FileField(upload_to='stocks/')),
>>>>>>> 68bccf09 (renames structure)
            ],
        ),
    ]
