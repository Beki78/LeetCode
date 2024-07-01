var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] === target - nums[i]) {
        return [i, j];
      }
    }
  }
};
