#include <stdlib.h>
#include <stdio.h>
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main()
{
    int N;    
    scanf("%d", &N);
    int strengths[N];
    for (int i = 0; i < N; i++) {
        int pi;
        scanf("%d", &pi);
        strengths[i] = pi;
    }

    qsort(strengths, N, sizeof(int), cmpfunc);

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    int delta = abs(strengths[0] - strengths[1]);
    for (int i = 0; i < N - 1; i++) {
        if (abs(strengths[i] - strengths[i + 1]) < delta)
            delta = abs(strengths[i] - strengths[i + 1]);
    }
    printf("%d\n", delta);
    return 0;
}
