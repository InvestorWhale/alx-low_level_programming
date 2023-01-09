#/bin/bash
gcc -wall -psdantic -Werror -Wextra -c *.c
ar rc liball.a *.o
