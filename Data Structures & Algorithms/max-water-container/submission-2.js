class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {    
        let left = 0;
        let right = heights.length - 1;
        let maxWater = 0;

        while (left < right) {
            const currentWidth = right - left;
            const currentHeight = Math.min(heights[left], heights[right]);
            const currentWater = currentWidth * currentHeight;

            maxWater = Math.max(maxWater, currentWater);

            // Move the pointer that points to the shorter bar
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
}
