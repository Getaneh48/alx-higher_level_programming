#include "lists.h"
#include <stdio.h>

/**
* check_cycle - check if there is a loop in the linked list.
* @list: single linked list
* Return: 1 Loop exist 0 Loop free
*/
int check_cycle(listint_t *list)
{
	int i = 0, j = 0, loop = 0;
	listint_t *temp = list, *curr = list;

	while (curr != NULL)
	{
		if (i > 0)
		{
			temp = list;
			j = 0;
			while (j < i)
			{
				if (temp == curr->next)
				{
					loop = 1;
					break;
				}
				temp = temp->next;
				j++;
			}
			if (loop)
				break;
		}
		curr = curr->next;
		i++;
	}

	return (loop);
}
