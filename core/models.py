from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Count

DjangoUser = get_user_model()


class User(DjangoUser):
    class Meta:
        proxy = True


def person_directory_path(instance: models.Model, filename: str) -> str:
    return 'avatar/person_{0}/{1}'.format(instance.id, filename)


class UserProfile(models.Model):
    GENDER = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255, blank=True)
    gender = models.CharField('Пол', max_length=10, choices=GENDER, null=True, blank=True)
    birth_date = models.DateField('Дата рождения')
    photo = models.ImageField('Фото', upload_to=person_directory_path, blank=True)

    class Meta:
        abstract = True

    def get_fullname(self) -> str:
        return ' '.join(filter(bool, [self.last_name, self.first_name, self.patronymic]))

    def __str__(self):
        return self.get_fullname()


class Teacher(UserProfile):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        related_name='teacher_profile'
    )
    subjects = models.ManyToManyField(
        'Subject',
        verbose_name='Предмет',
        related_name='teachers',
        through='TeacherSubject',
        through_fields=('teacher', 'subject'),
        blank=True
    )
    clubs = models.ManyToManyField(
        'Club',
        verbose_name='Кружок',
        related_name='club_teachers',
        through='TeacherSubject',
        through_fields=('teacher', 'club'),
        blank=True
    )
    replacement = models.ManyToManyField(
        'self',
        verbose_name='Замена',
        symmetrical=False,
        related_name='replacements',
        help_text='Заменяющие преподаватели',
        blank=True
    )

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Subject(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> str:
        return self.name


class Club(Subject):
    class Meta:
        proxy = True
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель',
        related_name='teacher_subjects'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name='Предмет',
        related_name='teacher_subjects',
        blank=True
    )
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        verbose_name='Кружок',
        related_name='teacher_clubs',
        blank=True,
    )
    dc = models.DateField('Дата начала ведения', default=date.today)

    class Meta:
        verbose_name = 'Ведение предмета/кружка'
        verbose_name_plural = 'Ведение предметов/кружков'


class Pupil(UserProfile):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        related_name='pupil_profile'
    )
    grade = models.ForeignKey(
        'Grade',
        on_delete=models.CASCADE,
        verbose_name='Класс',
        related_name='pupils',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class GradeManager(models.Manager):
    def with_count_pupils(self):
        return self.annotate(count_pupils=Count('pupils'))


class Grade(models.Model):
    grade_id = models.BigAutoField(primary_key=True)
    numeral = models.SmallIntegerField('Число', validators=[MinValueValidator(1), MaxValueValidator(11)])
    character = models.CharField('Буква', max_length=1)
    objects = GradeManager()

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        unique_together = ['numeral', 'character']

    def __str__(self) -> str:
        return f'{self.numeral}{self.character}'


class Tutor(Teacher, Grade):
    class Meta:
        verbose_name = 'Класс с тьютором'
        verbose_name_plural = 'Классы с тьютором'
    pass
