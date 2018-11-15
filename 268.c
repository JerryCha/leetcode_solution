int missingNumber(int* nums, int numsSize) {
    int i;
    int sortedNum[numsSize+1];
    for (i = 0; i < numsSize + 1; i++)
        sortedNum[i] = i + 1;
    for (i = 0; i < numsSize; i++)
        sortedNum[*(nums+i)] = *(nums+i);
    int num;
    for (i = 0; i < numsSize + 1; i++) {
        if (sortedNum[i] != i)
            num = i;
    }
    return num;
}
