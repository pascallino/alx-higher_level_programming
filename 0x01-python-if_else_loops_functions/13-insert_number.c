#include "lists.h"
#include <stdio.h>
/**
 * insert_node - sorted singly-linked list.
 * @head: head of the linked list.
 * @number: data
 * Return: If the function fails - NULL. else newnode is returned
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *newnode;

	curr = *head;
	newnode = (listint_t *)malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL || curr->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (*head);
	}
	while (curr->next && newnode && curr->next->n < number)
	{
		curr = curr->next;
	}
	newnode->next = curr->next;
	curr->next = newnode;
	return (newnode);
}


