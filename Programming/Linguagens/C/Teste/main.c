#include "read_num.c"
#include "utils.c"

int	main(int argc, char **argv)
{
	if (argc != 2)
		return (1);

	read_number(argv[1]);
	return (0);
}
