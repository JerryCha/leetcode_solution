void merge(int* nums1, int m, int* nums2, int n) {
    int i;
    int j = 0;
    int dynSize = m;
    for (i = 0; i < n; i++) {
        printf("i: %d ", i);
        while (j < dynSize && *(nums2+i) > *(nums1+j)) {
            j++;
        }
        printf("j: %d\n", j);
        int k;
        for (k=m+n-1; k > j; k--)
            *(nums1+k) = *(nums1+k-1);
        *(nums1+j) = *(nums2+i);
        dynSize++;
    }
}
