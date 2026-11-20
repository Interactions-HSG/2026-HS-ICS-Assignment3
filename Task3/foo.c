#include <stdio.h>

// A function that you need to implement
int foo(int n)
{
    /* Implement this code block */
}

/* Section for the Instrumentation Option used by GCC (no need to modify this)
 *
 * The __attribute__() is used to specify the special attribute "no_instrument_function" for the functions
 * cf. https://gcc.gnu.org/onlinedocs/gcc-3.4.2/gcc/Function-Attributes.html
 *
 * By implementing these two specific "profiling" functions, GCC is able to capture entry to and exit from functions
 * - void __cyg_profile_func_enter (void *this_fn, void *call_site);
 * - void __cyg_profile_func_exit  (void *this_fn, void *call_site);
 * cf. https://gcc.gnu.org/onlinedocs/gcc-4.4.7/gcc/Code-Gen-Options.html
 *
 */
__attribute__((no_instrument_function)) void __cyg_profile_func_enter(void *this_fn, void *call_site)
{
    printf(" --> %p %p\n", this_fn, call_site);
}
__attribute__((no_instrument_function)) void __cyg_profile_func_exit(void *this_fn, void *call_site)
{
    printf(" <-- %p %p\n", this_fn, call_site);
}

int main()
{
    for (int i = 0; i < 5; ++i)
    {
        printf("(%d) = %d\n", i, foo(i));
    }

    return 0;
}
