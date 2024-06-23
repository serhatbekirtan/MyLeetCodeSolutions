import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> compliments = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            Integer complimentIndex = compliments.get(nums[i]);
            if (complimentIndex != null){
                return new int[]{i, complimentIndex};
            }
            compliments.put(target - nums[i], i);
        }
        return nums;
    }
}