from django.db.models import Count

from core import models


def some_methods():
    qs1 = models.Grade.objects.aggregate(count_pupils=Count('pupils'))
    print(qs1)

    qs2 = models.Pupil.objects.first()
    print(qs2)

    grade_list = ['Математика', 'Алгебра', 'Информатика']
    grade_tuple = ('Математика', 'Алгебра', 'Информатика')
    grade_set = {'Математика', 'Алгебра', 'Информатика'}
    grade_dict = {'Математика': 0, 'Алгебра': 1, 'Информатика': 2}
    qs3_1 = models.Subject.objects.filter(name__in=grade_list)
    qs3_2 = models.Subject.objects.filter(name__in=grade_tuple)
    qs3_3 = models.Subject.objects.filter(name__in=grade_set)
    qs3_4 = models.Subject.objects.filter(name__in=grade_dict)
    print(qs3_1 == qs3_1)
    print(qs3_1)
    print(qs3_2)
    print(qs3_1 == qs3_2)
    print(qs3_3)
    print(qs3_4)
    print(qs3_3 == qs3_4)

