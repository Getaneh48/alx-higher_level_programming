#include "lists.h"

/**
* check_cycle - check if there is a loop in the linked list.
* @list: single linked list
* Return: 1 Loop exist 0 Loop free
*/
int check_cycle(listint_t *list)
{
	listint_t *prev, *next, *curr;

	while (curr != NULL)
	{
		prev = curr;
		next = curr->next;
		if (prev == next->next)
			return (1);

		curr = curr->next;
	}

	return (0);
}
