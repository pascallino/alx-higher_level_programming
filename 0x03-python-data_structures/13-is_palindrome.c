#include <stdio.h>
#include "lists.h"
/* define the struct */
int is_palindrome(listint_t **head);
/* 1 -> 2-> 3 -> 2 -> 1 -> NULL */
/**
 * is_palindrome - ==========
 * @head: ===================
 * Return: ==============
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *curr_ = *head;
	int curr2[arr];
	int i = 0;
	int is_palindrome = 1;

	if (curr->next == NULL || curr == NULL || !curr)
		return (is_palindrome);

	while (curr)
	{
	/*	printf("%d --> ", curr->age); */
		curr2[i] = curr->n;
		curr = curr->next;
		i++;
	}
	i--;
	/* lets compare the reversed array and list now */
	while (curr_)
	{
		if (curr2[i] != curr_->n)
		{
			is_palindrome = 0;
			return (is_palindrome);
		}
		curr_ = curr_->next;
		i--;
	}
	return (is_palindrome);
}
