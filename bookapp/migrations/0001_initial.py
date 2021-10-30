# Generated by Django 3.2.8 on 2021-10-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.TextField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para_id', models.IntegerField()),
                ('content', models.TextField()),
                ('sentence', models.TextField()),
                ('image', models.ImageField(upload_to='books/')),
                ('book', models.ForeignKey(db_column='book_id', on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookapp.book')),
            ],
        ),
    ]