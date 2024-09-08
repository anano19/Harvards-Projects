// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t *buffer = malloc(HEADER_SIZE);
    if (buffer == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // TODO: Read samples from input file and write updated data to output file
    fread(buffer, HEADER_SIZE, 1, input);
    fwrite(buffer, HEADER_SIZE, 1, output);

    float volume_factor = 2.0;
    int16_t sample;
    printf("Starting to read samples...\n");
    int counter = 0;

    while (fread(&sample, sizeof(int16_t), 1, input) == 1)
    {
        float float_sample = sample * volume_factor;
        if (float_sample > 32767.0f)
        {
            sample = 32767;
        }
        else if (float_sample < -32768.0f)
        {
            sample = -32768;
        }
        else
        {
            sample = (int16_t) float_sample;
        }

        counter++;
        if (counter % 10000 == 0) // Reduce the frequency of progress updates
        {
            printf("Processed %i samples\n", counter);
        }

        fwrite(&sample, sizeof(int16_t), 1, output);
    }

    free(buffer);
    // Close files
    fclose(input);
    fclose(output);
}
