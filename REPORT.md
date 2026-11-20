# Assignment 3 — Report

> **How to use this file.** This file *is* your hand-in. Edit it directly (in your editor, in
> your browser, or in Codespaces) and commit your changes.
>
> Every place you need to write something contains a line starting with `TODO:`.
> Replace that whole line with your answer. When no `TODO:` lines are left, the
> **Submission check** in the Actions tab turns green.
>
> Do not rename this file, and do not delete the `##` / `###` headings — we grade against them.

---

## 0. Team & process

You work in your assigned group of two. Both names go here, whoever created the repository.

| Field | Your entry |
| --- | --- |
| Group number | TODO: |
| Team member 1 (last name, first name) | TODO: |
| Team member 2 (last name, first name) | TODO: |

### 0.1 Roles

Who did what? One or two sentences per person.

TODO: replace this line with your answer.

### 0.2 Pitfalls

What were the major pitfalls you ran into, and how did you get past them?

TODO: replace this line with your answer.

### 0.3 Time spent

Roughly how many hours did this assignment take the two of you in total?

TODO: replace this line with your answer.

### 0.4 AI usage

You may use AI as a collaborator in this assignment. Which tools did you use, and for what?
Was there anything it got wrong that you had to check or correct?

TODO: replace this line with your answer.

---

## 1. Set Up Your Raspberry Pi (2pt)

Install Raspberry Pi OS and reach your Pi over the network — follow
[`docs/PI-SETUP.md`](docs/PI-SETUP.md). Then run `gcc --version` **on the Pi** and save a
screenshot of the terminal as [`screenshots/t1.png`](screenshots/).

### 1.1 Which gcc version runs on your Pi?

Copy the first line that `gcc --version` prints.

TODO: replace this line with your answer.

---

## 2. Dynamic Memory Allocation in C (1pt)

```c
int *pointer = (int *) malloc(sizeof(int) * 5);
```

### 2.1 How much memory is allocated? (0.25pt)

How many bytes are allocated at `pointer` if this code runs on your Raspberry Pi?

TODO: replace this line with your answer.

### 2.2 `malloc()` versus `calloc()` (0.25pt)

At least four key differences between the two.

TODO: replace this line with your list.

### 2.3 `realloc()` (0.25pt)

Code that uses `realloc()` to increase the capacity of `pointer` by 4 bytes:

```c
TODO: your code here
```

Compare this with allocating the memory using `calloc()`. What are the behavioural differences
between the two methods?

TODO: replace this line with your answer.

### 2.4 `free()` (0.25pt)

What is `free()` used for?

TODO: replace this line with your answer.

An example:

```c
TODO: your code here
```

---

## 3. Code Comprehension and Profiling (3.75pt)

### 3.1 `-fsanitize` (0.25pt)

What is GCC's `-fsanitize` program instrumentation option for? Which common sanitizers are
there, and which ones are effective for detecting **null pointers**, **use-after-free**, and
**data races**?

TODO: replace this line with your answer.

### 3.2 a) Reading the stack (1.0pt)

The value of `string_on_stack`, decoded from the stack bytes in Listing 1 of the sheet:

TODO: replace this line with your answer.

The words of the stack that hold it, as they appear in the listing (little-endian):

TODO: e.g. `0x........` `0x........` ...

The word (4 bytes) of the stack that shows the address where the value of `string_on_heap` is
stored:

TODO: e.g. `0x........`

### 3.2 b) Warnings and memory leaks (0.5pt)

Your corrected code is [`Task3/stack_and_heap.c`](Task3/stack_and_heap.c).

Why does compiling the original code result in the warning
`'free' called on unallocated object 'string_on_stack'`?

TODO: replace this line with your answer.

All lines of the original code that cause the warnings and the memory leaks:

```c
TODO: the lines here
```

What did you change, and why?

TODO: replace this line with your answer.

### 3.2 c) Buffer overflow (1.0pt)

Save a screenshot of the stack's memory bytes showing the buffer overflow as
[`screenshots/t3_2c.png`](screenshots/).

The string you entered to cause the buffer overflow:

TODO: replace this line with your answer.

Why does running the code with that input result in a segmentation fault?

TODO: replace this line with your answer.

### 3.3 Memory traces (1.0pt)

**a)** What is the function `foo` calculating (see Listing 2 of the sheet), and how exactly is
this implemented?

TODO: replace this line with your answer.

**b)** Your answer is the code in [`Task3/foo.c`](Task3/foo.c), plus a screenshot of its output
as [`screenshots/t3_3.png`](screenshots/) — nothing to write here.

---

## 4. Matrix-Matrix Multiplication using Dynamic Memory Allocation (1.5pt)

Your answer is the code in
[`Task4/matrix_multiplication.c`](Task4/matrix_multiplication.c) — nothing to write here.
Explain how your multiplication function works, and how to compile and run the program, in
comments in that file.

---

## 5. Performance Analysis (1.75pt)

Your code is [`Task5/calculate_gflops.c`](Task5/calculate_gflops.c). Run it on the Raspberry Pi
and on your own machine, plot the GFLOPS against the matrix size for each, and save the two
plots as [`screenshots/t5_rpi.png`](screenshots/) and [`screenshots/t5_local.png`](screenshots/).

### 5.1 Your own machine

Which computer did you use as "your own machine" (model, processor, operating system, compiler)?

TODO: replace this line with your answer.

### 5.2 Do GFLOPS decline as the matrix size increases?

If so, why does this happen?

TODO: replace this line with your answer.

### 5.3 The performance achieved on both devices

Explain the performance (in terms of GFLOPS) you measured on the Raspberry Pi and on your own
machine.

TODO: replace this line with your answer.

### 5.4 Optimizing the GFLOPS

What are possible ways of optimizing the GFLOPS for matrix multiplication and other
computations?

TODO: replace this line with your answer.

---

## Before you submit

- [ ] No `TODO:` lines left in this file
- [ ] `screenshots/` holds `t1.png`, `t3_2c.png`, `t3_3.png`, `t5_rpi.png` and `t5_local.png`
- [ ] `Task3/stack_and_heap.c` corrected, `Task3/foo.c` implemented
- [ ] `Task4/matrix_multiplication.c` written, with comments on how it works and how to run it
- [ ] `Task5/calculate_gflops.c` completed
- [ ] Everything **committed and pushed**
- [ ] Your partner **and** `lukabekavac` **and** `Karimkh31` added as collaborators
- [ ] **One** of you submitted the repository URL on Canvas (not both)
