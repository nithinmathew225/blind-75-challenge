class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 2. Sort the intervals based on their starting times.
        # This is crucial because it allows us to process intervals sequentially
        # and only compare adjacent or potentially overlapping intervals.
        # We use a lambda function to specify sorting by the first element (start time).
        intervals.sort(key=lambda x: x[0])

        # 3. Initialize the list to store merged intervals.
        # Start by adding the very first interval from the sorted list.
        merged = []
        merged.append(intervals[0])

        # 4. Iterate through the rest of the sorted intervals (starting from the second one).
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            # Get the last interval currently in the merged list.
            last_merged_start, last_merged_end = merged[-1]

            # 5. Check for overlap.
            # An overlap occurs if the start of the current interval is less than
            # or equal to the end of the last merged interval.
            if current_start <= last_merged_end:
                # Overlap found! Merge the current interval with the last merged interval.
                # The start of the merged interval remains `last_merged_start`.
                # The end of the merged interval becomes the maximum of the two ends.
                # Update the end of the *last interval* in the merged list.
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # No overlap. The current interval starts after the last merged interval ends.
                # Add the current interval as a new, separate interval to the merged list.
                merged.append([current_start, current_end])

        # 6. Return the list of merged intervals.
        return merged
            
