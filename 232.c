typedef struct {
    int* stack;
    int num;
    int maxSize;
} MyStack;

/** Initialize your data structure here. */
MyStack* myStackCreate(int maxSize) {
    MyStack* stack = (MyStack*)malloc(sizeof(MyStack));
    stack->num = 0;
    stack->maxSize = maxSize;
    stack->stack = (int*)malloc(sizeof(int)*maxSize);
    return stack;
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    obj->num++;
    *(obj->stack+obj->num) = x;
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack* obj) {
    int n = *(obj->stack+obj->num);
    obj->num--;
    return n;
}

/** Get the top element. */
int myStackTop(MyStack* obj) {
    return *(obj->stack + obj->num);
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack* obj) {
    return obj->num == 0 ? true : false;
}

void myStackFree(MyStack* obj) {
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * struct MyStack* obj = myStackCreate(maxSize);
 * myStackPush(obj, x);
 * int param_2 = myStackPop(obj);
 * int param_3 = myStackTop(obj);
 * bool param_4 = myStackEmpty(obj);
 * myStackFree(obj);
 */
