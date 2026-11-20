#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double timeTaken;
clock_t start;

// Calculate GFLOPS and time taken to perform matrix multiplication function
void calculate_gflops(int s)
{
    // Start time
    start = clock();

    /*
     * Enter your code to profile
     */

    // Enter the code to calculate time taken to perfom matrix multiplication divided by CLOCKS_PER_SEC: the number of seconds used by CPS */
    timeTaken = 0;

    // Enter the code to calculate the number of operations  performed by a matrix multiplication.
    double NumOps = 0;

    // Enter the code to calculate the GFLOPS : number of floating point operations per second in giga.
    double gflops = 0;

    // Print size of matrix, time taken by the matrix multiplication, and the GFLOPS performed.
    printf("%d\t%f\t%f\n", s, timeTaken, gflops);
}

int main()
{

    // Result titles printed once
    printf("Size \t Time Taken \t GFLOPS\n");

    for (int s = 1; s < 1000; s++)
    {
        /*
         *
         * Enter your code for matrix initialization and use s as the size of the matrix
         *
         */

        calculate_gflops(s);
    }

    return 0;
}
