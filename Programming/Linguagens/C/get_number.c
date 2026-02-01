#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc != 2)
		return (1);

	char *number = argv[1];
	int len = 0;

	/* tamanho */
	while (number[len])
		len++;

	for (int i = 0; i < len; i++)
	{
		char digit = number[i];

		/* valida dígito */
		if (digit < '0' || digit > '9')
			return (1);

		/* ignora zero */
		if (digit == '0')
			continue;

		int zeros = len - i - 1;

		/* imprime: digit - scale */
		printf("%c - ", digit);

		if (zeros == 0)
		{
			printf("1");
		}
		else
		{
			printf("1");
			while (zeros--)
				printf("0");
		}

		printf(" ");
	}

	printf("\n");
	return (0);
}
