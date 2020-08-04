from django.shortcuts import render, redirect
from django.views import View

from .sort_engine import Bubble, Insertion, Merge, Qsort
from .forms import SortForm
from .models import SortAlgorithms, TestCases, create_tests


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
        unsorted_seq = None
        sorted_seq = None
        check = False


        if bound_form.is_valid():

            sort_class = SORT_CLASSES[bound_form.cleaned_data['Algorithm_type']]
            sort_obj = sort_class()
            if not TestCases.CREATED:
                create_tests()
            cases = TestCases.objects.all()
            case_list = []
            for case in cases:
                case_list.append(case)
            raw_case = case_list[0].unsorted_numbers
            print(raw_case)
            sort_obj.unsorted_list = raw_case.split(' ')
            sort_obj.unsorted_list = [int(item) for item in sort_obj.unsorted_list]
            sort_obj.result, sort_obj.run_time = sort_obj.sort_list()
            # print(sort_obj.result)
            # print(sort_obj.run_time)

            new_model_obj = SortAlgorithms(
                Algorithm_type=bound_form.cleaned_data['Algorithm_type'],
                unsorted_seq=raw_case,
                sorted_seq=sort_obj.result,
                work_time=sort_obj.run_time,
                test_check=False
            )

            new_model_obj.save()
            unsorted_seq = raw_case
            sorted_seq = sort_obj.result

            # return redirect(new_model_obj)
        return render(request, self.template, context={
            'form': bound_form,
            'unsorted_seq': unsorted_seq,
            'sorted_seq': sorted_seq,
            'check': check
        })

