#include "read_num.h"

int	ft_strlen(char *s)
{
	int i = 0;
	while (s[i])
		i++;
	return (i);
}

int	ft_strnum_cmp(char *a, char *b)
{
	int i = 0;
	int len_a = ft_strlen(a);
	int len_b = ft_strlen(b);

	if (len_a > len_b)
		return (1);
	if (len_a < len_b)
		return (-1);

	while (a[i] && b[i])
	{
		if (a[i] > b[i])
			return (1);
		if (a[i] < b[i])
			return (-1);
		i++;
	}
	return (0);
}
