#include <stdio.h>
#include <stdlib.h>

typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;

int is_palindrome(listint_t** head) {
    // Edge case: Empty list
    if (*head == NULL || (*head)->next == NULL) {
        return 1;
    }

    listint_t* slow = *head;
    listint_t* fast = *head;
    listint_t* prev = NULL;
    listint_t* mid = NULL;
    int isPalindrome = 1;

    // Find the middle node using slow and fast pointers
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    // Handle odd length by skipping the middle node
    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    prev->next = NULL;
    listint_t* secondHalf = reverseList(slow);

    // Compare the first and second halves of the linked list
    listint_t* p1 = *head;
    listint_t* p2 = secondHalf;
    while (p1 != NULL && p2 != NULL) {
        if (p1->data != p2->data) {
            isPalindrome = 0;
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    // Restore the original linked list by reversing the second half again
    prev->next = reverseList(secondHalf);
    if (mid != NULL) {
        prev->next->next = mid;
    } else {
        prev->next->next = NULL;
    }

    return isPalindrome;
}

// Helper function to reverse a linked list
listint_t* reverseList(listint_t* head) {
    listint_t* prev = NULL;
    listint_t* current = head;
    listint_t* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

// Helper function to create a new node
listint_t* newNode(int data) {
    listint_t* node = (listint_t*)malloc(sizeof(listint_t));
    node->data = data;
    node->next = NULL;
    return node;
}

int main() {
    listint_t* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(2);
    head->next->next->next->next = newNode(1);

    int result = is_palindrome(&head);

    if (result == 1) {
        printf("Linked list is a palindrome.\n");
    } else {
        printf("Linked list is not a palindrome.\n");
    }

    // Clean up memory
    while (head != NULL) {
        listint_t* temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
