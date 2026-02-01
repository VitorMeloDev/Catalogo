#include <stdio.h>
#include "read_num.h"

#include "read_num.h"

int	get_scale(char *num)
{
	if (ft_strnum_cmp(num, "1000000000000000000") >= 0)
		return (18); // quintillion (exemplo)
	if (ft_strnum_cmp(num, "1000000000000000") >= 0)
		return (15);
	if (ft_strnum_cmp(num, "1000000000000") >= 0)
		return (12);
	if (ft_strnum_cmp(num, "1000000000") >= 0)
		return (9);
	if (ft_strnum_cmp(num, "1000000") >= 0)
		return (6);
	if (ft_strnum_cmp(num, "1000") >= 0)
		return (3);
	return (0);
}

static void	print_zeros(int n)
{
	printf("1");
	while (n-- > 0)
		printf("0");
}

void	read_number(char *num)
{
	int len = ft_strlen(num);
	int i = 0;

	while (i < len)
	{
		if (num[i] == '0')
		{
			i++;
			continue;
		}

		int remaining = len - i;
		int scale = get_scale(num + i);

		if (scale >= 3 && remaining > scale)
		{
			int digits = remaining - scale;
			int j = 0;

			while (j < digits)
			{
				printf("%c", num[i + j]);
				j++;
			}
			printf(" - ");
			print_zeros(scale);
			printf(" ");

			i += digits;
		}
		else
		{
			printf("%c - ", num[i]);
			print_zeros(remaining - 1);
			printf(" ");
			i++;
		}
	}
	printf("\n");
}
