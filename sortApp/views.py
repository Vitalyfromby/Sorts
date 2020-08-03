from django.shortcuts import render, redirect
from django.views import View

from .sort_engine import Bubble, Insertion, Merge, Qsort
from .forms import SortForm
from .models import SortAlgorithms


SORT_CLASSES = {
        1: Bubble,
        2: Insertion,
        3: Merge,
        4: Qsort,
}


def handle_uploaded_file(f):

    with open('media/data.txt', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    data = []
    with open('media/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
    for item in parts:
        data.append(int(item))
    return data


class SortView(View):
    model = SortAlgorithms
    template = 'input.html'
    form_class = SortForm
    sort_type = None

    def get(self, request):
        form = self.form_class()

        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_class(request.POST, request.FILES)

        if bound_form.is_valid():

            sort_class = SORT_CLASSES[bound_form.cleaned_data['Algorithm_type']]
            sort_obj = sort_class()
            sort_obj.unsorted_file = request.FILES['unsorted_numbers']
            sort_obj.unsorted_list = handle_uploaded_file(request.FILES['unsorted_numbers'])
            sort_obj.result, sort_obj.run_time = sort_obj.sort_list()
            print(sort_obj.result)
            print(sort_obj.run_time)

            new_model_obj = SortAlgorithms(
                Algorithm_type=bound_form.cleaned_data['Algorithm_type'],
                unsorted_numbers=sort_obj.unsorted_file,
                sorted_result=sort_obj.result,
                work_time=sort_obj.run_time
            )

            new_model_obj.save()

            # return redirect(new_model_obj)
        return render(request, self.template, context={'form': bound_form})

