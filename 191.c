int hammingWeight(uint32_t n) {
    int bits = 0 + countBit(n);
    return bits;
}
int countBit(uint32_t n) {
    if (n != 0)
        return n%2==1?1+countBit(n/2):countBit(n/2);
    return 0;
}
