# LeetCode Quiz 19 - 从单链表中移除倒数第N个节点

> Given a linked list, remove the n-th node from the end of list and return its head.
>
> Given linked list: 1->2->3->4->5, and n = 2.
>
> After removing the second node from the end, the linked list becomes 1->2->3->5.

## 题目分析

这道题属于单链表的双指针应用。因为单链表只能从头部进入，在数据结构的定义中如果不包含节点总数，那么想在单个循环通过计数法找到目标节点是一件困难的事情（至少通过常规操作是不可能的事情）。非常不巧的是，LeetCode的单链表定义只包含了当前节点的payload以及下一节点的指针，我们没法在一个循环内用计数法找到目标节点。

```py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

## 那就遍历两边

说实话，对于这道题而言，两个循环也不是那么的不堪，时间复杂度至少还是$O(n)$。

对于单链表节点删除，惯用紧紧跟随的两个指针，当表示当前位置的指针走到被删除节点时，前一指针可以轻松的将它的下一节点指向当前指针的下一节点。

### 第一趟循环

第一趟循环的主要目的是统计到底有多少个节点，这趟循环从头结点开始，到指针移出链表结束。总共使用一个指针。

### 第二趟循环

第二趟循环的目的是找到需要删除的节点，循环依然从头节点开始，到倒数第N个节点为止。这回需要使用两个指针，分别将它们命名为当前指针`curr`和前一指针`prev`。

从链表头算起，倒数第*N*个节点是正数第*n-N+1*个节点。`curr`需要向前移动  *n-N*  次。

```py
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # 假如传入的是一个空链表
    if head is None:
        return head
    # 创建一个变量统计到底有多少个节点
    numOfNodes = 0
    # 创建一个指针表示目前处在的位置，起始位置为头结点head
    curr = head
    # 不断向前，直到脱离链表为止
    while curr is not None:
        numOfNodes += 1
        curr = curr.next
    # 完成统计，指针回头
    curr = head
    # 创建另一个指针，代表当前指针的前一节点
    prev = None
    # 将当前指针和前一指针向前移动 numOfNodes - N 遍，每次前进一个节点
    for _ in range(numOfNodes-n):
        prev = curr
        curr = curr.next
    # 如果不能前进，那就删掉头结点（LeetCode定义行为）
    if prev is None:
        return head.next
    prev.next = curr.next
    return head
```

## 能不能一遍过?

### 将两个指针隔开一定的距离

这算是单链表中一遍过时比较常规的操作，通过另一个指针延迟出发并保持一定的速度，来定位“倒数第N个节点”。

我们定义三个指针

* `front`： 前指针
* `back`： 后指针
* `backPrev`：后指针指向的节点的前一节点指针

把终止条件设为`front`脱离链表，`back`指针要保持多远的距离才能走到正确的位置呢？答案是n。实践上，下面这段代码每一轮循环都会对n减1，并通过n的值控制`back`和`backPrev`的步进。

```py
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # 前指针
    front = head
    # 后指针
    back = None
    # 后指针的前一指针
    backPrev = None
    while front != None:
        # 每一轮循环的起始自减，代表curr在上一轮前进了一步，
        # 也因为curr是直接从head开始，即循环初始条件下curr已经走出了第一步。
        n -= 1
        # 计数，如果没到合适的间距，back不出发
        if n == 0:
            back = head
        # 计数，值为零代表back已经抵达head，那么值为 -1 时backPrev出发，并不断追随back
        elif n < 0:
            backPrev = back
            back = back.next
        front = front.next
    # back没出发或是backPrev没出发，代表着删除第一个节点或者n大于实际节点数的情况
    # LeetCode没有给出当传入超出范围的n的具体行为。经实际测试是删除头结点。
    if back is None or backPrev is None:
        return head.next
    # 双指针删除节点法
    backPrev.next = back.next
    return head
```

## 太麻烦了，这么多代码

众所周知，递归法往往可以将复杂的迭代法代码精简到只有几行。

通过一个额外的函数，这个函数接受同样的参数，返回一个整数。每一轮递归调用时，将下一个节点、n传入，直到节点的`next`指向`None`为止（base case）。

到了base case后该怎么办？直接返回n-1就好。如果不在base case，那我们就检测下一递归调用送回来的n-1到底是不是0，是的话，将它的`next`调到`next.next`就好。

```py
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    n = self.recursiveWay(head, n)
    if n >= 0:
        return head.next
    return head

def recursiveWay(self, head: ListNode, n: int) -> int:
    if head.next is not None:
        n = self.recursiveWay(head.next, n)
    if n == 0:
        head.next = head.next.next
    return n-1
```
