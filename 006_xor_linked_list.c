#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

TODO: Figure out how to xor pointers safely in C (line 45, try uintptr_t?)
*/

// Build with: gcc 006_xor_linked_list.c -o xor_linked_list

typedef struct xor_ll_node_t {
    int val;
    struct xor_ll_node_t* both;
} xor_ll_node_t;

void xor_ll_add(xor_ll_node_t** head, int val)
{
    xor_ll_node_t *prev, *next, *iter;

    // First node addition
    if ((*head) == NULL) {
        (*head) = malloc(sizeof(xor_ll_node_t));
        (*head)->val = val;
        (*head)->both = NULL;
    } else {
        // Add 2nd node
        if ((*head)->both == NULL) {
            next = malloc(sizeof(xor_ll_node_t));
            next->val = val;
            next->both = (*head);
            (*head)->both = next;
        } else {
            // Add nth node

            // Set iter to 2nd node
            prev = (*head);
            iter = (*head)->both;

            // Traverse to end of list
            while (iter->both != prev) {
                iter = prev ^ iter->both;
            }
        }
    }
}

bool xor_ll_get(xor_ll_node_t* head, int index, int* val)
{
    xor_ll_node_t* iter = head;
    xor_ll_node_t *next, *prev;
}

int main()
{
    xor_ll_node_t* head;
    int val;

    xor_ll_add(&head, 1);
    xor_ll_add(&head, 2);
    xor_ll_add(&head, 3);

    if (xor_ll_get(head, 0, &val) == true) {
        if (val == 1) {
            printf("Okay!");
        }
    }
    if (xor_ll_get(head, 1, &val) == true) {
        if (val == 2) {
            printf("Okay!");
        }
    }
    if (xor_ll_get(head, 2, &val) == true) {
        if (val == 3) {
            printf("Okay!");
        }
    }

    return 0;
}
