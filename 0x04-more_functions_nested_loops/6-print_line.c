#include "main.h"

/**
 * print_line - print _ * n
 * @n: number  of _ to print
 */

void print_line(int n)
{
	int i;

	c = 0;
	while (c < n)
	{
		_putchar('_');

		c++;
	}
	_putchar('\n');
}
