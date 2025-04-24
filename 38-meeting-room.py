"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) <= 1:
            return True

        # Sort the intervals based on their start times (the first element of the tuple).
        # This allows checking only adjacent intervals for overlaps.
        intervals.sort(key=lambda x: x[0]) 

        # Iterate through the sorted intervals, starting from the second one.
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            previous_end = intervals[i-1][1]

            # Check for overlap: If the current meeting starts strictly BEFORE 
            # the previous meeting ends, there's a conflict.
            # Note: If current_start == previous_end, it's not a conflict (e.g., (0,8) and (8,10)).
            if current_start < previous_end:
                return False  # Conflict found

        # If the loop finishes without returning False, it means no conflicts were found.
        return True
