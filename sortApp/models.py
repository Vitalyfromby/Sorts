from django.db import models


class TestCases(models.Model):

    TESTS_COUNT = 5
    CREATED = False

    unsorted_numbers = models.TextField(verbose_name='unsorted_seq')
    sorted_numbers = models.TextField(verbose_name='sorted_seq')

    class Meta:
        verbose_name_plural = 'Cases'
        verbose_name = 'Case'


def create_test():
    from random import randint

    unsorted_list = []

    count = randint(5, 15)
    for val in range(count):
        unsorted_list.append(randint(-100, 100))

    unsorted_case = [str(item) for item in unsorted_list]
    unsorted_case = ' '.join(unsorted_case)
    sorted_case = sorted(unsorted_list)
    sorted_case = [str(item) for item in sorted_case]
    sorted_case = ' '.join(sorted_case)

    TestCases.objects.create(unsorted_numbers=unsorted_case, sorted_numbers=sorted_case)


def create_tests():
    for i in range(TestCases.TESTS_COUNT):
        create_test()
    TestCases.CREATED = True


def delete_cases():

    TestCases.objects.all().delete()
    TestCases.CREATED = False


class SortAlgorithms(models.Model):

    TYPES = (
        (1, 'Bubble'),
        (2, 'Insertion'),
        (3, 'Merge'),
        (4, 'Qsort'),

    )

    Algorithm_type = models.IntegerField(choices=TYPES, default=TYPES[0], blank=False,
                                         null=False, verbose_name='Type of algorithm')
    unsorted_seq = models.TextField(verbose_name='unsorted', default='')
    sorted_seq = models.TextField(verbose_name='sorted', default='')
    worked_at = models.DateTimeField(auto_now_add=True)
    work_time = models.FloatField(null=True)
    test_check = models.BooleanField(verbose_name='test_checked', default=False)

    class Meta:
        verbose_name_plural = 'Sort_info'
        verbose_name = 'Sort_info'
        ordering = ['-worked_at']

