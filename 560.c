int subarraySum(int* nums, int numsSize, int k) {
    int cumSum[numsSize+1];
    int i;
    cumSum[0] = 0;
    for (i = 1; i <= numsSize; i++)
        cumSum[i] = cumSum[i-1] + *(nums+i-1);
    
    int j;
    int count = 0;
    for (i = 0; i < numsSize; i++)
        for (j = i+1; j <= numsSize; j++)
            if (cumSum[j] - cumSum[i] == k)
                count++;
    return count;
}
