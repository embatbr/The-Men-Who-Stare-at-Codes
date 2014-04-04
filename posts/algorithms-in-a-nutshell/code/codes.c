#include <stdio.h>
#include <stdlib.h>

void code01(void)
{
    int numbers[] = {1, 2, 3, 4, 5};
    int sum = 0;
    int i = 0;
    int len = sizeof(numbers) / sizeof(int);

    while(i < len)
    {
        sum = sum + numbers[i];
        i++;
    }

    printf("sum: %d\n", sum);
}


// linked list

typedef struct list LIST;
struct list
{
    int value;
    LIST *next;
};

LIST * gen_list(int size)
{
    LIST *head = malloc(sizeof(LIST));
    head->value = 1;
    LIST *tail = head;

    int i;
    for(i = 1; i < size; i++)
    {
        tail->next = malloc(sizeof(LIST));
        tail->next->value = i + 1;
        tail = tail->next;
    }

    return head;
}

void code02(void)
{
    LIST *list = gen_list(3);

    while(list != 0)
    {
        printf("%d\n", list->value);
        list = list->next;
    }
}


// queue

void enqueue(LIST *queue, int value)
{
    while(queue->next != 0)
    {
        queue = queue->next;
    }

    queue->next = malloc(sizeof(LIST));
    queue->next->value = value;
}

void code03(void)
{
    LIST *queue = gen_list(3);
    LIST *head = queue;

    printf("queue:\n");
    while(queue != 0)
    {
        printf("%d\n", queue->value);
        queue = queue->next;
    }

    queue = head;
    enqueue(queue, 4);

    printf("enqueue element 4:\n");
    while(queue != 0)
    {
        printf("%d\n", queue->value);
        queue = queue->next;
    }

    printf("dequeue element %d:\n", head->value);
    head = head->next;
    queue = head;
    while(queue != 0)
    {
        printf("%d\n", queue->value);
        queue = queue->next;
    }
}


// stack

LIST * push(LIST *stack, int value)
{
    LIST *new_element = malloc(sizeof(LIST));
    new_element->value = value;
    new_element->next = stack;

    return new_element;
}

void code04(void)
{
    LIST *stack = gen_list(3);
    LIST *head = stack;

    printf("stack:\n");
    while(stack != 0)
    {
        printf("%d\n", stack->value);
        stack = stack->next;
    }

    stack = push(head, 0);
    head = stack;

    printf("push element 0:\n");
    while(stack != 0)
    {
        printf("%d\n", stack->value);
        stack = stack->next;
    }

    printf("pop element 0:\n");
    head = head->next;
    stack = head;
    while(stack != 0)
    {
        printf("%d\n", stack->value);
        stack = stack->next;
    }
}


int main(void)
{
    code01();
    printf("\n");
    code02();
    printf("\n");
    code03();
    printf("\n");
    code04();
    return 0;
}