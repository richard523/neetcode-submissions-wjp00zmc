from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # List to store all valid IP addresses found
        results = []
        # Get the length of the input string, used for boundary checks
        n = len(s)

        # Helper function to validate if a string segment is a valid IP part
        def is_valid_part(segment_str):
            # An empty segment is not valid
            if not segment_str:
                return False
            # Check for leading zeros: "01" is invalid, but "0" is valid
            if len(segment_str) > 1 and segment_str[0] == '0':
                return False
            # Convert segment to integer and check if it's within the valid range [0, 255]
            num = int(segment_str)
            return 0 <= num <= 255

        # Backtracking function to explore all possible IP address combinations
        # start_idx: The current index in the string 's' from which to form the next segment
        # current_parts: A list of string segments formed so far for the current IP address candidate
        def backtrack(start_idx, current_parts):
            # Base case 1: If we have successfully formed 4 segments
            if len(current_parts) == 4:
                # Check if all characters from the original string 's' have been used
                if start_idx == n:
                    # If yes, join the segments with dots and add the complete IP address to results
                    results.append(".".join(current_parts))
                return # Return regardless, as 4 segments are formed and we either found a solution or not

            # Pruning 1: If we've exhausted the string but haven't formed 4 parts yet, this path is invalid
            if start_idx == n:
                return

            # Pruning 2: Check if it's still possible to form the remaining segments
            # Each remaining segment must be at least 1 digit and at most 3 digits long.
            remaining_segments = 4 - len(current_parts)
            min_len_needed = remaining_segments * 1 # Minimum total length required for remaining segments
            max_len_needed = remaining_segments * 3 # Maximum total length allowed for remaining segments
            remaining_str_len = n - start_idx # Actual length of the remaining string

            # If the remaining string length is too short or too long for the remaining segments, prune this path
            if not (min_len_needed <= remaining_str_len <= max_len_needed):
                return

            # Iterate to try forming the next segment
            # A segment can be 1, 2, or 3 digits long
            for length in range(1, 4):
                # Calculate the end index (exclusive) for the current segment
                end_idx = start_idx + length

                # Ensure the segment does not go beyond the string's end
                if end_idx > n:
                    break # No more characters left to form a segment of this length, so break the loop

                # Extract the current segment string
                segment = s[start_idx : end_idx]

                # Validate the current segment using the helper function
                if is_valid_part(segment):
                    # If valid, add it to the current IP parts list
                    current_parts.append(segment)
                    # Recursively call backtrack for the next segment, starting from the new end_idx
                    backtrack(end_idx, current_parts)
                    # Backtrack: remove the last segment to explore other possibilities (undo the choice)
                    current_parts.pop()

        # Start the backtracking process from the beginning of the string (index 0) with an empty list of parts
        backtrack(0, [])
        # Return the list of all valid IP addresses found
        return results

