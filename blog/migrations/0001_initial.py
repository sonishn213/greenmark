# Generated by Django 4.1.7 on 2023-03-05 14:49

from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_grid',
            fields=[
                ('Url', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='category/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.CharField(default=None, max_length=50, unique=True)),
                ('category', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', djrichtextfield.models.RichTextField()),
                ('quote', models.TextField()),
                ('quoteauthor', models.CharField(max_length=100)),
                ('othimage', models.ImageField(blank=True, default='default.png', upload_to='post/')),
                ('authorpic', models.ImageField(blank=True, default='default.png', upload_to='post/')),
                ('aboutauthor', models.TextField()),
                ('fb_url', models.CharField(default=None, max_length=255)),
                ('t_url', models.CharField(default=None, max_length=255)),
                ('insta_url', models.CharField(default=None, max_length=255)),
                ('Url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Urls', to='blog.blog_grid')),
            ],
        ),
    ]
