from __future__ import annotations
from typing import Generator
import time
from .metrics import SortMetrics


def insertion_sort(arr: list[int]) -> tuple[list[int], SortMetrics]:
    """Insertion sort with metric tracking."""
    a = arr.copy()
    m = SortMetrics()
    start = time.perf_counter()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            m.comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                m.swaps += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    m.time_ms = (time.perf_counter() - start) * 1000
    return a, m


def merge_sort(arr: list[int]) -> tuple[list[int], SortMetrics]:
    """
    Merge sort with metric tracking.
    Uses recursion and operator overloading when combining metrics.
    """
    start = time.perf_counter()
    sorted_arr, metrics = _merge_sort_inner(arr.copy())
    metrics.time_ms = (time.perf_counter() - start) * 1000
    return sorted_arr, metrics


def _merge_sort_inner(a: list[int]) -> tuple[list[int], SortMetrics]:
    """Internal merge sort that returns metrics without timing."""
    if len(a) <= 1:
        return a, SortMetrics()

    mid = len(a) // 2
    left, m_left = _merge_sort_inner(a[:mid])
    right, m_right = _merge_sort_inner(a[mid:])

    merged: list[int] = []
    i = j = 0
    m = m_left + m_right  # operator overloading (__add__)

    while i < len(left) and j < len(right):
        m.comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, m


def bubble_sort_steps(arr: list[int]) -> Generator[list[int], None, SortMetrics]:
    """
    Generator function that yields the list after each swap.
    Returns SortMetrics at the end.
    """
    a = arr.copy()
    m = SortMetrics()
    start = time.perf_counter()

    n = len(a)
    if n <= 1:
        m.time_ms = (time.perf_counter() - start) * 1000
        return m

    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            m.comparisons += 1
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                m.swaps += 1
                swapped = True
                yield a.copy()
        n -= 1

    m.time_ms = (time.perf_counter() - start) * 1000
    return m
