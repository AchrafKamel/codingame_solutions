#include <stdlib.h>
#include <stdio.h>
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    // the number of temperatures to analyse
    int n;
    scanf("%d", &n);
    int temperatures[n];
    for (int i = 0; i < n; i++) {
        // a temperature expressed as an integer ranging from -273 to 5526
        int t;
        scanf("%d", &t);
        temperatures[i] = t;
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    int closest_to_zero = temperatures[0];
    for (int i = 0; i < n; i++)
    {
        if (abs(temperatures[i]) < abs(closest_to_zero))
            closest_to_zero = temperatures[i];
        else if (temperatures[i] == -closest_to_zero)
            closest_to_zero = abs(temperatures[i]);
    }

    printf("%d\n", closest_to_zero);

    return 0;
}
