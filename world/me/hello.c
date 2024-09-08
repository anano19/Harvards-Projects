#include <stdio.h>
#include <cs50.h>
int main(void)
{
    string s;
    s = get_string("hello, whats your name? ");
    printf("hello, %s\n", s);
}
