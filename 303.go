type NumArray struct {
    sumArray []int
}


func Constructor(nums []int) NumArray {
    arr := new(NumArray)
    arr.sumArray = make([]int, len(nums)+1)
    arr.sumArray[0] = 0
    for i:= 1; i < len(arr.sumArray); i++ {
        arr.sumArray[i] = arr.sumArray[i-1] + nums[i-1]
    }
    return *arr
}


func (this *NumArray) SumRange(i int, j int) int {
    j++
    return this.sumArray[j] - this.sumArray[i]
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(i,j);
 */
