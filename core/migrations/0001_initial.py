# Generated by Django 5.0.1 on 2024-02-11 15:12

import core.models
import datetime
import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=10, null=True, verbose_name='Пол')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, upload_to=core.models.person_directory_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=10, null=True, verbose_name='Пол')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, upload_to=core.models.person_directory_path, verbose_name='Фото')),
                ('replacement', models.ManyToManyField(blank=True, help_text='Заменяющие преподаватели', related_name='replacements', to='core.teacher', verbose_name='Замена')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('numeral', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)], verbose_name='Число')),
                ('character', models.CharField(max_length=1, verbose_name='Буква')),
                ('pupils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='core.pupil', verbose_name='Ученики')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'unique_together': {('numeral', 'character')},
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
            ],
            options={
                'verbose_name': 'Кружок',
                'verbose_name_plural': 'Кружки',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.subject',),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('grade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.grade')),
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.teacher')),
            ],
            options={
                'verbose_name': 'Класс с тьютором',
                'verbose_name_plural': 'Классы с тьютором',
            },
            bases=('core.teacher', 'core.grade'),
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc', models.DateField(default=datetime.date.today, verbose_name='Дата начала ведения')),
                ('subject', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subjects', to='core.subject', verbose_name='Предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subjects', to='core.teacher', verbose_name='Преподаватель')),
                ('club', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_clubs', to='core.club', verbose_name='Кружок')),
            ],
            options={
                'verbose_name': 'Ведение предмета/кружка',
                'verbose_name_plural': 'Ведение предметов/кружков',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='teachers', through='core.TeacherSubject', to='core.subject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='teacher_profile', to='core.user', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='pupil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='pupil_profile', to='core.user', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='clubs',
            field=models.ManyToManyField(blank=True, related_name='club_teachers', through='core.TeacherSubject', to='core.club', verbose_name='Кружок'),
        ),
    ]