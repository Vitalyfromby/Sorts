from django.db import models


class SortAlgorithms(models.Model):

    TYPES = (
        (1, 'Bubble'),
        (2, 'Insertion'),
        (3, 'Merge'),
        (4, 'Qsort'),

    )

    Algorithm_type = models.IntegerField(choices=TYPES, default=TYPES[0], blank=False,
                                         null=False, verbose_name='Type of algorithm')
    unsorted_numbers = models.FileField(upload_to='documents/')
    sorted_result = models.TextField(verbose_name='result')
    worked_at = models.DateTimeField(auto_now_add=True)
    work_time = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Sort_info'
        verbose_name = 'Sort_info'
        ordering = ['-worked_at']

