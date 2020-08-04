from django.contrib import admin

from .models import SortAlgorithms, TestCases


class SortAlgorithmsAdmin(admin.ModelAdmin):
    list_display = ('Algorithm_type', 'unsorted_seq', 'sorted_seq', 'work_time', 'worked_at', 'test_check')


admin.site.register(SortAlgorithms, SortAlgorithmsAdmin)


class TestCasesAdmin(admin.ModelAdmin):
    list_display = ('unsorted_numbers', 'sorted_numbers')


admin.site.register(TestCases, TestCasesAdmin)

