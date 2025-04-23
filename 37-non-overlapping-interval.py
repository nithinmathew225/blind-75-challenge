class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on their END times in ascending order.
        # This greedy approach works because choosing the interval that finishes
        # earliest leaves the maximum amount of room for subsequent intervals.
        # If two intervals have the same end time, their relative order doesn't
        # affect the correctness of this specific greedy approach.
        intervals.sort(key=lambda x: x[1])

        # Initialize the count of non-overlapping intervals we can keep.
        # We always keep the first interval in the sorted list (the one ending earliest).
        count_kept = 1
        # Keep track of the end time of the last interval we decided to keep.
        last_kept_end = intervals[0][1]

        # Iterate through the rest of the sorted intervals, starting from the second one.
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            # Check if the current interval starts AFTER or exactly AT the end
            # of the last interval we kept. If it does, they don't overlap.
            # Note: Intervals like [1,2] and [2,3] are considered non-overlapping.
            if current_start >= last_kept_end:
                # No overlap found. We can keep this current interval.
                count_kept += 1
                # Update the end time of the last kept interval to the end of the current one.
                last_kept_end = current_end
            # else (current_start < last_kept_end):
                # Overlap found. We must "remove" one of the overlapping intervals.
                # The greedy strategy based on sorting by end times ensures that we
                # keep the one that finished earlier (which is the one associated with
                # `last_kept_end`). Therefore, we implicitly "remove" the current
                # interval by simply not incrementing `count_kept` and not updating
                # `last_kept_end`.

        # The minimum number of removals required is the difference between the
        # total number of intervals and the maximum number we could keep.
        total_intervals = len(intervals)
        min_removals = total_intervals - count_kept

        return min_removals
        
