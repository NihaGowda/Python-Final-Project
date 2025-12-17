from src.algorithms import insertion_sort, merge_sort


def test_insertion_sort_correct():
    arr = [3, 1, 2]
    original = arr.copy()
    sorted_arr, m = insertion_sort(arr)

    assert sorted_arr == [1, 2, 3]
    assert arr == original  # input should not be modified
    assert m.comparisons >= 0
    assert m.swaps >= 0
    assert m.time_ms >= 0


def test_merge_sort_correct():
    arr = [5, 4, 3, 2, 1]
    original = arr.copy()
    sorted_arr, m = merge_sort(arr)

    assert sorted_arr == [1, 2, 3, 4, 5]
    assert arr == original  # input should not be modified
    assert m.comparisons >= 0
    assert m.swaps >= 0
    assert m.time_ms >= 0


def test_sorts_handle_duplicates_and_negatives():
    arr = [0, -1, 3, 3, 2, -1]
    ins_sorted, _ = insertion_sort(arr)
    mer_sorted, _ = merge_sort(arr)

    assert ins_sorted == sorted(arr)
    assert mer_sorted == sorted(arr)


def test_already_sorted_input():
    arr = [1, 2, 3, 4, 5]
    ins_sorted, _ = insertion_sort(arr)
    mer_sorted, _ = merge_sort(arr)

    assert ins_sorted == [1, 2, 3, 4, 5]
    assert mer_sorted == [1, 2, 3, 4, 5]
