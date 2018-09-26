#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: double pointer to head node
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return(NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return(head);
	}

	for (tmp = *head; tmp->next != NULL; tmp = tmp->next)
	{
		if (new_node->n < (tmp->n))
		{
			
		}
	}
}
