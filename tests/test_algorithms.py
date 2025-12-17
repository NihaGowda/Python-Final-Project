from src.algorithms import insertion_sort, merge_sort


def test_insertion_sort_correct():
    arr = [3, 1, 2]
    sorted_arr, m = insertion_sort(arr)
    assert sorted_arr == [1, 2, 3]
    assert m.comparisons >= 0
    assert m.swaps >= 0


def test_merge_sort_correct():
    arr = [5, 4, 3, 2, 1]
    sorted_arr, m = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]
    assert m.comparisons >= 0
