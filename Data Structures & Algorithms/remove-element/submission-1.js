class Solution {
	removeElement(nums, val) {
        const tmp = [];
        for (const num of nums) {
            if (num !== val) {
                tmp.push(num)
                }
            }
        
        for (let i = 0; i < tmp.length; i++) {
            nums[i] = tmp[i];
        }
        return tmp.length;
    }
}