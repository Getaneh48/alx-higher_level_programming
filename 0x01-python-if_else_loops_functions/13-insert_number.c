#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
* insert_node - inserts a new node
* @head: head of the list
* @number: value of the new node
*
* Return: the address of the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node = NULL, *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (current == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	while (current != NULL)
	{
		if (number < current->n)
		{
			new_node->n = number;
			if (prev == NULL)
			{
				new_node->next = current;
				*head = new_node;
			}
			else
			{
				new_node->next = prev->next;
				prev->next = new_node;
			}
			break;
		}
		prev = current;
		current = current->next;
	}
	if (current == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		prev->next = new_node;
	}

	return (new_node);
}
