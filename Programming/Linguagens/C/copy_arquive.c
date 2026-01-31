#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	int		fd;
	int		bytes;
    int     i;
	char	buffer[128];

	char	*content = NULL; // onde vamos guardar tudo
	int		size = 0;        // tamanho atual armazenado

	if (argc != 2)
		return (1);

	fd = open(argv[1], O_RDONLY);
	if (fd < 0)
		return (1);

    while ((bytes = read(fd, buffer, 128)) > 0)
    {
        char *tmp = malloc(size + bytes);
        if (!tmp)
            return (1);

        int i = 0;
        while (i < size)
        {
            tmp[i] = content[i];
            i++;
        }

        i = 0;
        while (i < bytes)
        {
            tmp[size + i] = buffer[i];
            i++;
        }

        free(content);
        content = tmp;
        size += bytes;
    }
	close(fd);

	// imprime tudo de uma vez
	if (content)
	{
		write(1, content, size);
		free(content);
	}
}