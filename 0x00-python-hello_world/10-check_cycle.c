#include "lists.h"
#include <stdio.h>

/**
* a function in C that checks if a singly linked list has a cycle in it
* @list: list
* Return: 0 if there is no cycle, 1 if there is a cycle
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
