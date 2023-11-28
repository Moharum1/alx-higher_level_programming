#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - add a new element to a sorted node
 * @head: pointer to head of list
 * @number: number we want to add to the node
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *future;

	current = *head;
	future =  current->next;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		current = new;

	if (current->n > new->n)
	{
		new->next = current
		current = new;
	}
	else
	{
		while (future != NULL)
		{
			if (number < future->n)
			{
				current->next = new;
				new->next = future;
				return (new);
			}
			future = future->next;
			current = current->next;
		}
		current->next = new;
	}
	return (NULL);
}

