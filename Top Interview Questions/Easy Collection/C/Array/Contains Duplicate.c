int compare(const void *a, const void *b)
{
      int c = *(int *)a;
      int d = *(int *)b;
      if(c < d) {return -1;}
      else if (c == d) {return 0;}
      else return 1;
}

bool containsDuplicate(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    for(int i=0; i<numsSize-1; i++){
        if(nums[i]==nums[i+1]){
            return true;
        }
    }
    return false;
}
