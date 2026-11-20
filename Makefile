# Assignment 3 -- Memory Management
#
#   make all              compile everything into build/ -- "does it all compile?"
#   make valgrind         compile Task3/stack_and_heap.c, run it under Valgrind   (Task 3.2 b)
#   make gdb              compile Task3/stack_and_heap.c for debugging, open gdb   (Task 3.2 c)
#   make foo              compile Task3/foo.c with -finstrument-functions, run it  (Task 3.3)
#   make matrix           compile Task4/matrix_multiplication.c                    (Task 4)
#   make gflops           compile Task5/calculate_gflops.c                         (Task 5)
#   make clean            remove build artifacts
#
# These are the same commands as in docs/PI-SETUP.md, only shorter. Run them on the
# Raspberry Pi (and, for Task 5, on your own machine too).
#
# No `make` on Windows? Use the commands in docs/PI-SETUP.md instead.

CC    := gcc
BUILD := build

PROGRAMS := stack_and_heap foo matrix_multiplication calculate_gflops

.PHONY: all valgrind gdb foo matrix gflops clean

# Compile each program into build/ -- used by the submission check.
all: $(addprefix $(BUILD)/,$(PROGRAMS))

$(BUILD):
	@mkdir -p $(BUILD)

# -g -O0: debug information and no optimisation, so the stack looks the way the code reads.
$(BUILD)/stack_and_heap: Task3/stack_and_heap.c | $(BUILD)
	$(CC) -g -O0 $< -o $@

# -g -Og: what the sheet uses for Valgrind, so its report can name line numbers.
$(BUILD)/stack_and_heap_valgrind: Task3/stack_and_heap.c | $(BUILD)
	$(CC) -g -Og $< -o $@

# -finstrument-functions makes gcc call the two profiling functions in foo.c on every
# function entry and exit.
$(BUILD)/foo: Task3/foo.c | $(BUILD)
	$(CC) -finstrument-functions $< -o $@

$(BUILD)/matrix_multiplication: Task4/matrix_multiplication.c | $(BUILD)
	$(CC) $< -o $@ -lm

# -lm links the math library.
$(BUILD)/calculate_gflops: Task5/calculate_gflops.c | $(BUILD)
	$(CC) $< -o $@ -lm

valgrind: $(BUILD)/stack_and_heap_valgrind
	@command -v valgrind >/dev/null || (echo "valgrind not found -- on the Pi: sudo apt install valgrind"; exit 1)
	valgrind ./$<

gdb: $(BUILD)/stack_and_heap
	@command -v gdb >/dev/null || (echo "gdb not found -- on the Pi: sudo apt install gdb"; exit 1)
	gdb ./$<

foo: $(BUILD)/foo
	./$<

matrix: $(BUILD)/matrix_multiplication
	@echo
	@echo "  Built $<  -- run it with ./$<"
	@echo

gflops: $(BUILD)/calculate_gflops
	@echo
	@echo "  Built $<"
	@echo "  Run it and keep the numbers:  ./$< | tee results.tsv"
	@echo "  On the Pi this can take an hour or more."
	@echo

clean:
	rm -rf $(BUILD)
