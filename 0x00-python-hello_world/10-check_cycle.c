#include "lists.h"
/**
 * check_cycle - tortoise and hare, but we need to find the loop
 * @head: Pointer to the head node
 * Return: 1 or 0
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			slow = head;
			while (slow && fast)
			{
				if (slow == fast)
					return (1);
				slow = slow->next;
				fast = fast->next;
			}
		}
	}
	return (0);
}
