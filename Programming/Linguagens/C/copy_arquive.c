#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

char	*read_file(int fd, int *out_size)
{
	char	buffer[128];
	char	*content = NULL;
	char	*tmp;
	int		size = 0;
	int		bytes;
	int		i;

	while ((bytes = read(fd, buffer, 128)) > 0)
	{
		tmp = malloc(size + bytes);
		if (!tmp)
			return (NULL);

		i = 0;
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

	*out_size = size;
	return (content);
}

int	main(int argc, char **argv)
{
	int		fd;
	int		size;
	char	*content;

	if (argc != 2)
		return (1);

	fd = open(argv[1], O_RDONLY);
	if (fd < 0)
		return (1);

	content = read_file(fd, &size);
	close(fd);

	if (!content)
		return (1);

	write(1, content, size);
	free(content);

	return (0);
}
