#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check if the user provided exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Validate that the key is a positive integer
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Key must be a positive integer.\n");
            return 1;
        }
    }

    // Convert the key from a string to an integer
    int key = atoi(argv[1]);

    // Get the plaintext from the user
    string name = get_string("plaintext: ");

    // Encrypt the plaintext
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        if (isalpha(name[i]))
        {
            // Shift lowercase letters
            if (islower(name[i]))
            {
                name[i] = ((name[i] - 'a' + key) % 26) + 'a';
            }
            // Shift uppercase letters
            else if (isupper(name[i]))
            {
                name[i] = ((name[i] - 'A' + key) % 26) + 'A';
            }
        }
    }

    // Print the ciphertext
    printf("ciphertext: %s\n", name);
    return 0;
}
