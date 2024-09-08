#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            int average = (int) round((red + green + blue) / 3.0);

            // Update pixel values to grayscale
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            float sepiaRed = 0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue;
            float sepiaGreen = 0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue;
            float sepiaBlue = 0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue;

            int roundedRed = (int) round(sepiaRed);
            int roundedGreen = (int) round(sepiaGreen);
            int roundedBlue = (int) round(sepiaBlue);

            // Cap values at 255
            if (roundedRed > 255)
                roundedRed = 255;
            if (roundedGreen > 255)
                roundedGreen = 255;
            if (roundedBlue > 255)
                roundedBlue = 255;

            image[i][j].rgbtRed = roundedRed;
            image[i][j].rgbtGreen = roundedGreen;
            image[i][j].rgbtBlue = roundedBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width / 2; j++)
        {
            // Use a temporary variable to swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
