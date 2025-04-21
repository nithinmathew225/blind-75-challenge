class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval

        # Phase 1: Add all intervals ending strictly before newInterval starts
        # These intervals do not overlap with newInterval and come before it.
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals
        # Start with newInterval as the interval to potentially merge.
        merged_start = new_start
        merged_end = new_end

        # Iterate through intervals that *start* before or at the point the current
        # merged interval *ends*. This condition identifies intervals that could
        # possibly overlap with the interval being built.
        while i < n and intervals[i][0] <= merged_end:
            # Overlap detected (or interval is adjacent).
            # Merge the current interval into the merged interval by updating boundaries.
            merged_start = min(merged_start, intervals[i][0])
            merged_end = max(merged_end, intervals[i][1])
            i += 1 # Move to the next interval to check for further overlaps

        # Add the final merged interval (which includes the original newInterval
        # and any intervals it overlapped with) to the result.
        result.append([merged_start, merged_end])

        # Phase 3: Add remaining intervals
        # These intervals start strictly after the merged interval ends.
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        
