# Assignment 3: Memory Management

**Einführung in Computersysteme — HS 2026 · 10 points · Deadline: 13 December 2026, 23:59 CET**

You will explore **memory allocation and code profiling** in C: the heap and the stack, memory
leaks, a buffer overflow, and how fast your Raspberry Pi multiplies matrices. 📄 The questions
and all the detail are in **[`docs/assignment3.pdf`](docs/assignment3.pdf)**. This page is only
about *how to work and hand in*.

**You need:** a Raspberry Pi 400 PC-Kit with its SD card, and a Wi-Fi network that both your
computer and the Pi can join (your phone's hotspot works well).

**You work in your assigned group of two.** You share **one** repository: one of you creates
it, the other joins as a collaborator. Only one of you hands in.

**Same procedure as in Assignments 1 and 2** — but with a **new** repository. Do not reuse an
earlier one. If you have done this before, skim the steps; what changes is the template link,
the name `ics-a3-group<N>`, and that this time **your programs run on the Pi itself**.

*Original repository: <https://github.com/Interactions-HSG/2026-HS-ICS-Assignment3>*

---

## Step 1 · One of you makes the copy

> **Decide who does this — only one of you.** If your partner already created the repository,
> skip to Step 3 and ask them to add you.

On the [assignment repository](https://github.com/Interactions-HSG/2026-HS-ICS-Assignment3),
click the green **`Use this template`** → **`Create a new repository`**.

Then:

| Setting | What to choose |
| --- | --- |
| Repository name | `ics-a3-group<your number>`, e.g. **`ics-a3-group7`** |
| Visibility | **Private** ← important |

Your **group number** is the one from the group assignment on Canvas. Use digits only, no
spaces: `ics-a3-group7`, not `ics-a3-Group 7` or `ics-a3-gruppe7`. We match repositories to
groups by that name, so getting it right saves everyone time.

Click **Create repository**. Your group now has its repository at
`github.com/your-username/ics-a3-group7`.

> **Why not "Fork"?**
> You may have seen a **Fork** button on GitHub. Forking also copies a project, but a fork of
> a public project is **always public** — everyone in the course could read your answers.
> **Use this template** gives you a private copy instead. So: template, not fork.

## Step 2 · Add your partner and us

The repository is private, so right now *nobody* can see it — not your partner, not us. Whoever
created it goes to:

**Settings** → **Collaborators** → **Add people**, and adds **three** people:

```
<your partner's GitHub username>
lukabekavac
Karimkh31
```

Your partner then gets an email invitation and has to **accept** it before they can push.

> ⚠️ **Forget this and we cannot open your repository, so we cannot grade you.** Do it now, not
> on the deadline.

## Step 3 · Open your repository

This assignment is different from the first two: the programs are compiled and run **on the
Raspberry Pi**, which now has an operating system. So this time, working **on your own
computer** is the practical choice — it is on the same network as the Pi and can copy files to
it.

### Option A — On your own computer (recommended this time)

In a terminal:

```console
git clone https://github.com/your-username/ics-a3-group7.git
cd ics-a3-group7
```

`clone` means "download this repository onto my computer, and remember where it came from".
Use the URL of **your group's** repository, not the one you are reading now.

### Option B — Codespaces

In **your** repository: **`Code ▾`** → **`Codespaces`** → **`Create codespace on main`**.

A Codespace is good for writing `REPORT.md` and for checking that your C code compiles (`make
all`). But it lives in a data centre: it cannot reach your Pi, and it is not a Raspberry Pi. The
results, screenshots and measurements you hand in have to come from **your Pi** (and, for
Task 5, also from your own machine) — not from the Codespace.

💡 When you are done for the day, stop the Codespace (**`Code ▾` → `Codespaces` → `...` →
`Stop codespace`**) so it does not use up your free hours.

## Step 4 · Set up the Pi, then do the tasks

👉 **[`docs/PI-SETUP.md`](docs/PI-SETUP.md)** takes you through installing Raspberry Pi OS,
logging in over SSH, and copying files between your computer and the Pi. It also has every
command you need, task by task.

The loop for each task looks like this:

1. edit the code on your computer (in this repository),
2. copy it to the Pi and compile and run it there,
3. take the screenshot the task asks for and save it into `screenshots/`,
4. write your answer into **[`REPORT.md`](REPORT.md)**.

`REPORT.md`, together with your code and screenshots, *is* your hand-in — there is no zip file
and nothing to upload. Every place that needs an answer from you holds a line that starts with
`TODO:`. Replace that whole line with your answer. That's the entire trick.

| Task | Where your work goes |
| --- | --- |
| 1 | `screenshots/t1.png` |
| 3.2 b) | `Task3/stack_and_heap.c` |
| 3.2 c) | `screenshots/t3_2c.png` |
| 3.3 | `Task3/foo.c` and `screenshots/t3_3.png` |
| 4 | `Task4/matrix_multiplication.c` |
| 5 | `Task5/calculate_gflops.c`, `screenshots/t5_rpi.png` and `screenshots/t5_local.png` |
| all | your answers in `REPORT.md` |

## Step 5 · Save your work (this is what Git is for)

Editing a file is not enough — you have to **commit** it (take a snapshot) and **push** it
(upload that snapshot to GitHub). Until you push, we see nothing.

**In VS Code or Codespaces**, use the **Source Control** panel on the left (the branching icon):
type a short message, click **Commit**, then click **Sync Changes**. That's it.

**In a terminal**, the same thing in three commands:

```console
git add .                        # which changes go into the snapshot -- "." means all of them
git commit -m "Answered task 2"  # take the snapshot, with a short note about what you did
git push                         # upload it to GitHub
```

Do this often — after every task, not once at the end. It costs 10 seconds and it means a
crashed laptop cannot eat your evening.

> **Changed a file on the Pi?** Then the newest version is on the Pi, not in your repository.
> Copy it back to your computer first ([`docs/PI-SETUP.md`](docs/PI-SETUP.md) shows how), then
> commit and push.

> **Working with your partner:** you share one repository, so run `git pull` (or click
> **Sync Changes**) *before* you start working, to get their latest changes. If you both edit
> the same lines at the same time, Git will ask you to sort out the conflict — easiest to avoid
> by agreeing who does which task.

**Check it worked:** open your repository on github.com and look at `REPORT.md`. If your
answers are there, you are safe.

### You get automatic feedback

Every time you push, a check runs and tells you what is still missing: unanswered questions, a
missing screenshot, code you have not touched yet, code that does not compile. Click the
**Actions** tab of your repository to see it — a green ✓ means nothing is missing, a red ✗
tells you exactly what to fix.

It checks **completeness, not correctness**. Green does not mean your answers are right.

## Step 6 · Hand in

1. No `TODO:` lines left in `REPORT.md` — including your **group number** and **both names**
   at the top
2. Everything **pushed** (Step 5) — code, screenshots and report
3. Your partner, `lukabekavac` and `Karimkh31` added as collaborators (Step 2)
4. **One of you** — not both — submits **only the repository URL** on Canvas:
   `https://github.com/your-username/ics-a3-group7`

We grade whatever is on your `main` branch at the deadline. Both of you get the same mark.

---

## What's in this repository

| File | What it is |
| --- | --- |
| **`REPORT.md`** | **Your hand-in.** Answer the questions here. |
| `Task3/stack_and_heap.c` | **Task 3.2.** Given to you, incomplete and with errors — complete and correct it. |
| `Task3/foo.c` | **Task 3.3.** The function `foo` is empty — implement it. |
| `Task4/matrix_multiplication.c` | **Task 4.** Empty — your matrix multiplication goes here. |
| `Task5/calculate_gflops.c` | **Task 5.** A skeleton for timing your multiplication — complete it. |
| `screenshots/` | Put your five images here. |
| `docs/` | The assignment sheet, and the Pi setup and command guide. |
| `Makefile` | Build shortcuts: `make all`, `make valgrind` and friends. Works on the Pi, on macOS and on Linux. |

## Stuck?

- **[`docs/PI-SETUP.md`](docs/PI-SETUP.md)** — the commands for every task, and what to do when
  the Pi does not show up on the network.
- The [C memory management reference](https://en.cppreference.com/w/c/memory) — `malloc`,
  `calloc`, `realloc` and `free`, each on one page.
- The [Valgrind quick start](https://valgrind.org/docs/manual/quick-start.html) — how to read
  the heap summary.
- [How to look at the stack with gdb](https://jvns.ca/blog/2021/05/17/how-to-look-at-the-stack-in-gdb/)
  — a short tutorial for Task 3.2.
- **Using AI:** you may use it as a collaborator — to explain concepts, to help you read
  compiler, Valgrind and gdb output, and to debug. Whatever you hand in, you should understand
  and be able to explain yourself. Write down how you used it in section 0.4 of the report.
- Come to the exercise session, or ask in your repository's **Issues** tab and mention
  `@lukabekavac` or `@Karimkh31`.

## Contact

- Luka Bekavac — <luka.bekavac@unisg.ch> · GitHub `lukabekavac`
- Karim Khamaisi — <karim.khamaisi@unisg.ch> · GitHub `Karimkh31`
- Simon Mayer — <simon.mayer@unisg.ch>

## License

MIT — see [`LICENSE`](LICENSE).
