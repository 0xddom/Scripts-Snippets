import sys
import os

format_string = "char code[] = \"{0}\";"

clang_cmd = "clang -O2 -Wall -Wextra generated_test.c -o generated_test"
#clang_cmd = "cat generated_test.c"

f = open(sys.argv[1],'r')
s = f.read()[1:]
f.close()

s = ''.join('\\x%02x' % ord(i) for i in s)


output = open('generated_test.c', 'w')
output_s = format_string.format(s)
output_s = """#include <sys/mman.h>
#include <inttypes.h>
#include <unistd.h>
#include <stdio.h>

""" + output_s + """

int main()
{
    puts("Antes de ejecutar la shell");

    int (*ret)() = (int (*)())code;
    void *page = (void *)((uintptr_t)code & ~(getpagesize() - 1));

    mprotect(page, sizeof code, PROT_EXEC);
    ret();

    return 0;
}"""
output.write (output_s)
output.close()

comp_res = os.system(clang_cmd)
if comp_res == 0:
	os.system("./generated_test")
