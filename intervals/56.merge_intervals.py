from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    len_intervals = len(intervals)
    start_list = []
    end_list = []
    res = []
    for (start, end) in intervals:
        start_list.append(start)
        end_list.append(end)
    start_list.sort()
    end_list.sort()
    ptr = 0
    start = 0
    while ptr < len_intervals:
        while ptr < len_intervals - 1 and end_list[ptr] >= start_list[ptr+1]:
            ptr += 1
        res.append([start_list[start], end_list[ptr]])
        ptr += 1
        start = ptr
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
assert merge(intervals) == [[1,6],[8,10],[15,18]]


intervals = [[1,4],[4,5]]
assert merge(intervals) == [[1,5]]

