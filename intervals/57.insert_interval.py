from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        elif intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
    res.append(newInterval)
    return res

    # My solution
    
    # start = 0
    # while start < len(intervals) and newInterval[0] > intervals[start][1]:
    #     start += 1
    # if start == len(intervals):
    #     intervals.append(newInterval)
    #     return intervals
    # end = start
    # while end < len(intervals) and newInterval[1] >= intervals[end][0]:
    #     end += 1
    # end -= 1
    # if start > end:
    #     intervals.insert(start, newInterval)
    #     return intervals
    # intervals[start] = [min(intervals[start][0], newInterval[0]), max(intervals[end][1], newInterval[1])]
    # for _ in range(end-start):
    #     del intervals[start + 1]
    # print(intervals)
    # return intervals

intervals = [[1,3],[6,9]]
newInterval = [2,5]
assert insert(intervals, newInterval) == [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
assert insert(intervals, newInterval) == [[1,2],[3,10],[12,16]]
