#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * This program copies a value from the stack to the heap, where the string on the stack is string_on_stack and
 * string_on_heap is a pointer to the heap
 */
int main()
{
    // stack string initialization
    char string_on_stack[20] = ""; // Task 3.2 a): enter here the correct value, based on the stack bytes shown in the assignment pdf
    int n = 20;

    /*
     * Initialize the pointer to the heap
     * The size of the allocated memory depends on the value of n
     */
    char *string_on_heap = (char *)malloc(n);

    // Deallocate the memory
    free(string_on_stack);

    // Copy the value of string_on_stack to string_on_heap
    strcpy(string_on_heap, string_on_stack);

    // Print the value in the variable string_on_heap
    printf("string_on_heap is: %s\n", string_on_heap);

    // Ask users to enter a new value for string_on_stack
    printf("Enter new string_on_stack: ");
    scanf("%[^\n]s", string_on_stack);

    // Print the new string on stack and string on heap
    printf("New string_on_stack: %s and string_on_heap: %s\n", string_on_stack, string_on_heap);

    return 0;
}
