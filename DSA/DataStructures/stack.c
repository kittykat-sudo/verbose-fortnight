#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct{
    int arr[MAX_SIZE];
    int top;
} Cake;
void initialize(Cake *stack){
    stack->top = -1;
}
bool isempty(Cake *stack){
    return stack->top ==-1;
}
bool isfull(Cake *stack){
    return stack-> top == MAX_SIZE-1;
}

void push(Cake*stack , int value){
    if(isfull(stack)){
        printf("Stack overflow\n");
    }
    stack->arr[++stack->top] = value;
    printf("Added %d in to stack\n", value);
}
void pop(Cake*stack){
    if(isempty(stack)){
        printf("stack is empty nothing to pop\n");
    }
    int popped = stack->arr[stack->top];
    stack->top--;

    printf("popped %d\n", popped);
}
int peek(Cake*stack){
    printf("top %d\n",stack->arr[stack->top]);
}

int main() {
    Cake stack;
    initialize(&stack);
    push(&stack, 30);
    push(&stack, 89);
    pop(&stack);
    peek(&stack);
    
    

    return 0;
}