class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
    // Initialize the left pointer at the start (index 0)
    let left = 0;
    // Initialize the right pointer at the end (last index)
    let right = numbers.length - 1;

    // Continue searching as long as the pointers haven't crossed
    while (left < right) {
        const currentSum = numbers[left] + numbers[right];

        if (currentSum === target) {
            // Found the solution. Return 1-indexed results as required.
            return [left + 1, right + 1];
        } else if (currentSum < target) {
            // Sum is too small, move left pointer right to increase the sum.
            left++;
        } else { // currentSum > target
            // Sum is too large, move right pointer left to decrease the sum.
            right--;
        }
    }

    // This return is theoretically unreachable based on the problem constraints.
    return [];
}

}
