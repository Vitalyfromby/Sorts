from django import forms

from .models import SortAlgorithms


class SortForm(forms.ModelForm):

    class Meta:
        model = SortAlgorithms
        fields = ('Algorithm_type', 'unsorted_numbers')


