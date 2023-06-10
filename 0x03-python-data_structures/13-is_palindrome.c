#include <stdio.h>
#include "lists.h"

listint_t* reverseList(listint_t* head);
int is_palindrome(listint_t** head);

int is_palindrome(listint_t** head) 
{
	listint_t* p1;
	listint_t* secondHalf;
	listint_t* p2;
	listint_t* slow = *head;
	listint_t* fast = *head;
	listint_t* prev = NULL;
	listint_t* mid = NULL;
	int isPalindrome = 1;

	/* Edge case: Empty list */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle node using slow and fast pointers */
	while (fast != NULL && fast->next != NULL) 
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* Handle odd length by skipping the middle node*/
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	/*Reverse the second half of the linked list*/
	prev->next = NULL;
	secondHalf = reverseList(slow);

	/*Compare the first and second halves of the linked list*/
	p1 = *head;
	p2 = secondHalf;
	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n) {
			isPalindrome = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	/*Restore the original linked list by reversing the second half again*/
	prev->next = reverseList(secondHalf);
	if (mid != NULL)
	{
		prev->next->next = mid;
	}
	else
	{
		prev->next->next = NULL;
	}

	return (isPalindrome);
}

/* Helper function to reverse a linked list*/
listint_t* reverseList(listint_t* head)
{
	listint_t* prev = NULL;
	listint_t* current = head;
	listint_t* next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
