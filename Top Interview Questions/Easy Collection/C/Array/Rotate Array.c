void rotate(int* nums, int numsSize, int k){
    if(numsSize == 1)
        return;
    k %= numsSize;
    int temp;
    for(int i=0; i<numsSize/2; i++){
        temp = nums[i];
        nums[i] = nums[numsSize-1-i];
        nums[numsSize-1-i] = temp;
    }
    for(int i=0; i<k/2; i++){
        temp = nums[i];
        nums[i] = nums[k-1-i];
        nums[k-1-i] = temp;
    }
    for(int i=0; i<(numsSize-k)/2; i++){
        temp = nums[i+k];
        nums[i+k] = nums[numsSize-i-1];
        nums[numsSize-i-1] = temp;
    }
    return;
}
