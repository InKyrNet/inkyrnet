# Generated by Django 3.1.7 on 2021-03-14 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Технология',
                'verbose_name_plural': 'Технологии',
                'db_table': 'technology',
            },
        ),
        migrations.CreateModel(
            name='TypeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('type_time', models.CharField(choices=[('full-time', 'Полная занятость'), ('temporary', 'Временный'), ('internship', 'Стажировка'), ('freelance', 'Фриланс'), ('part-time', '\tЧастичная занятость'), ('another', 'Другое')], max_length=30, verbose_name='Выберите время')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Тип занятости',
                'verbose_name_plural': 'Типы занятости',
                'db_table': 'type_time',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_end', models.DateTimeField(verbose_name='Дата истечения')),
                ('price_min', models.CharField(max_length=30, verbose_name='Цена минимум')),
                ('price_max', models.CharField(max_length=30, verbose_name='Цена максимум')),
                ('experience', models.IntegerField(blank=True, default='1', verbose_name='Опыт(год)')),
                ('is_closed', models.BooleanField(default=True, verbose_name='Вакансия закрыта?')),
                ('is_premium_job', models.BooleanField(default=False, verbose_name='Премиум-вакансия?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('slug', models.SlugField(unique=True, verbose_name='Ярлык')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_job', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('bookmark', models.ManyToManyField(blank=True, related_name='user_bookmark_job', to=settings.AUTH_USER_MODEL, verbose_name='В избранных')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_city', to='events.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'db_table': 'job',
            },
        ),
    ]
