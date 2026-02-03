#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

int min3(int a, int b, int c)
{
	if (a <= b && a <= c)
		return (a);
	if (b <= a && b <= c)
		return (b);
	return (c);
}

void putnbr(int n)
{
	char c;

	if (n >= 10)
		putnbr(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

int main(void)
{
	int fd = open("map.txt", O_RDONLY);
	char buf;
	char map[100][100];
	int dp[100][100];
	int rows = 0;
	int cols = 0;
	int i = 0;
	int j = 0;

    int max = 0;
    int max_i = 0;
    int max_j = 0;


	if (fd < 0)
		return 1;

	/* leitura simples do mapa */
	while (read(fd, &buf, 1))
	{
		if (buf == '\n')
		{
			map[rows][i] = '\0';
			if (cols == 0)
				cols = i;
			i = 0;
			rows++;
		}
		else
			map[rows][i++] = buf;
	}
	close(fd);

	/* algoritmo do BSQ (só os números) */
	i = 0;
	while (i <= rows)
	{
		j = 0;
		while (j < cols)
		{
			if (map[i][j] == 'o')
				dp[i][j] = 0;
			else if (i == 0 || j == 0)
				dp[i][j] = 1;
			else
				dp[i][j] = 1 + min3(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
            if (dp[i][j] > max)
            {
                max = dp[i][j];
                max_i = i;
                max_j = j;
            }
			j++;
		}
		i++;
	}

    int i = max_i;
    while (i >= max_i - (max - 1)) 
    {
        int j = max_j;
        while (j >= max_j - (max - 1))
        {
            map[i][j] = 'x'; // full
            j--;
        }
        i--;
    }

	/* imprime a matriz de números */
	i = 0;
	while (i <= rows)
	{
		j = 0;
		while (j < cols)
		{
			putnbr(dp[i][j]);
			write(1, " ", 1);
			j++;
		}
		write(1, "\n", 1);
		i++;
	}

	return 0;
}
