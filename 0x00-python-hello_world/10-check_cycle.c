#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a linked list has cycle
 * @listint_t: pointer to the list yo want to free
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}

	return (0);
}
