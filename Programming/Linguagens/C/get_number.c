#include <stdio.h>

int main(void)
{
	char *number = "2363";
	int len = 0;
	int i = 0;

	/* descobre o tamanho */
	while (number[len])
		len++;

	while (i < len)
	{
		int zeros = len - i - 1;
		char digit = number[i];

		/* ignora zero */
		if (digit == '0')
		{
			i++;
			continue;
		}

		/* caso especial: 10–19 */
		if (zeros == 1 && digit == '1')
		{
			printf("%c%c ", number[i], number[i + 1]);
			i += 2;
			continue;
		}

		/* dezenas (20, 30, 40...) */
		if (zeros == 1)
		{
			printf("%c0 ", digit);
		}
		/* centenas ou mais (100, 1000, 10000...) */
		else if (zeros >= 2)
		{
			printf("%c", digit);
			printf("1");
			while (zeros--)
				printf("0");
			printf(" ");
		}
		/* unidade */
		else
		{
			printf("%c ", digit);
		}

		i++;
	}

	printf("\n");
	return (0);
}
