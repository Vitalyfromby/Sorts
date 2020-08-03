

def time_counter(func):
    import time

    def wrapped(*args):
        start_time = time.clock()
        return_value = func(*args)
        run_time = float(round((time.clock() - start_time), 9))
        print(run_time)
        return return_value, run_time

    return wrapped


class Algorithms:

    def __init__(self):
        self.unsorted_file = None
        self.unsorted_list = None
        self.result = None
        self.run_time = None


class Bubble(Algorithms):

    @time_counter
    def sort_list(self):

        last = len(self.unsorted_list)

        while last > 1:
            for index in range(0, last-1):
                if self.unsorted_list[index] > self.unsorted_list[index + 1]:
                    self.unsorted_list[index], self.unsorted_list[index + 1] = self.unsorted_list[index + 1], self.unsorted_list[index]
            last -= 1

        result = ' '.join([str(i) for i in self.unsorted_list])
        return result


class Insertion(Algorithms):

    @time_counter
    def sort_list(self):

        last = len(self.unsorted_list)
        for index in range(1, last):
            for check_index in range(0, index):
                if self.unsorted_list[index] < self.unsorted_list[check_index]:
                    self.unsorted_list.insert(check_index, self.unsorted_list.pop(index))

        result = ' '.join([str(i) for i in self.unsorted_list])
        return result


class Merge(Algorithms):

    @time_counter
    def sort_list(self):

        def merge(left_part, right_part):
            sorted_list = []
            left_part_index = right_part_index = 0

            left_part_length, right_part_length = len(left_part), len(right_part)

            for i in range(left_part_length + right_part_length):
                if left_part_index < left_part_length and right_part_index < right_part_length:

                    if left_part[left_part_index] <= right_part[right_part_index]:
                        sorted_list.append(left_part[left_part_index])
                        left_part_index += 1

                    else:
                        sorted_list.append(right_part[right_part_index])
                        right_part_index += 1

                elif left_part_index == left_part_length:
                    sorted_list.append(right_part[right_part_index])
                    right_part_index += 1

                elif right_part_index == right_part_length:
                    sorted_list.append(left_part[left_part_index])
                    left_part_index += 1

            return sorted_list

        def split(num_list):

            if len(num_list) <= 1:
                return num_list

            mid = len(num_list) // 2

            left_part = split(num_list[:mid])
            right_part = split(num_list[mid:])

            return merge(left_part, right_part)

        result = ' '.join([str(i) for i in split(self.unsorted_list)])
        return result


class Qsort(Algorithms):

    @time_counter
    def sort_list(self):
        import random

        num_list = self.unsorted_list

        def qsort(nums, fst, lst):
            if fst >= lst:
                return

            i, j = fst, lst
            pivot = nums[random.randint(fst, lst)]

            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i, j = i + 1, j - 1
            qsort(nums, fst, j)
            qsort(nums, i, lst)

        qsort(num_list, 0, len(num_list)-1)

        result = ' '.join([str(i) for i in self.unsorted_list])
        return result

