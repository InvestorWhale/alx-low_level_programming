#include "hash_tables.h"
/**
 * key_index - the index of the key that are calculated from the ht
 *
 * @key: the value that are stored in the index
 * @size: the size of the array
 * Return: the index of the array of the ht
 */

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
