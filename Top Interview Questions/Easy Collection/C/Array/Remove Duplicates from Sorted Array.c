int removeDuplicates(int* nums, int numsSize){
    if(numsSize == 0)
        return 0;
        
    int cur = nums[0];
    int next_idx = 1;
    for(int i=1; i<numsSize; i++){
        if(nums[i] != cur){
            nums[next_idx] = nums[i];
            cur = nums[i];
            next_idx++;
        }
    }
    return next_idx;
}