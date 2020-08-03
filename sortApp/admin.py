from django.contrib import admin

from .models import SortAlgorithms


class SortAlgorithmsAdmin(admin.ModelAdmin):
    list_display = ('Algorithm_type', 'unsorted_numbers', 'sorted_result', 'work_time', 'worked_at',)


admin.site.register(SortAlgorithms, SortAlgorithmsAdmin)
