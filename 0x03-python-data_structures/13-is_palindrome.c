#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* is_palindrome - check if a single list is
* a palindrome or not
*
* @head: head of the list
* Return: true or false
*/
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, list_len = 0, palindrome = 1;
	listint_t *h = NULL, **slist = NULL;

	if (head == NULL)
		return (palindrome);
	h = *head;
	while (h != NULL)
	{
		h = h->next;
		j++;
	}
	list_len = j - 1;
	slist = malloc(sizeof(listint_t) * list_len + 1);
	if (slist == NULL)
		exit(1);
	h = *head;
	while (h != NULL)
	{
		slist[i] = h;
		h = h->next;
		i++;
	}
	slist[list_len + 1] = NULL;
	i = 0, j = list_len;
	while (i < j)
	{
		if (slist[i]->n != slist[j]->n)
		{
			palindrome = 0;
			break;
		}
		i++;
		j--;
	}
	free(slist);
	return (palindrome);
}
