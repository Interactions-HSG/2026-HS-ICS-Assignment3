#!/usr/bin/env python3
"""Completeness check for an Assignment 3 hand-in.

This does NOT grade anything and never looks at whether an answer is *correct* --
it only tells the student which parts of the hand-in are still missing, so nobody
loses points to an oversight. Run it locally with:

    python3 .github/scripts/check_submission.py
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_REPO = "2026-HS-ICS-Assignment3"
REPO_PREFIX = "ics-a3-group"
GRADERS = ("lukabekavac", "Karimkh31")

# The code files as we hand them out: SHA-256 of the source with comments and
# whitespace removed (see `strip_c`). A file that still has this fingerprint has not
# been worked on. To regenerate after changing a starter file:
#
#     python3 .github/scripts/check_submission.py --fingerprints
STARTERS = {
    "Task3/stack_and_heap.c": (
        "4700a213040883a365737d67fc1e4cd040a51c5a9b915a993852af5fcfeadcab",
        "Task 3.2 asks you to complete it (the value of `string_on_stack`) and to fix "
        "the lines that cause the warnings and the memory leaks.",
    ),
    "Task3/foo.c": (
        "a6eb9b5382edac982cc223a0a11710158b87965a13bda151abf69d3f0cfa7be0",
        "Task 3.3 asks you to implement the function `foo`.",
    ),
    "Task4/matrix_multiplication.c": (
        "3bbb8fa08f5146dbe7fe3d0567f920ff568b3bc6d864b4b56648f2d0648ef7cd",
        "Task 4 asks you to write a matrix-matrix multiplication with dynamically "
        "allocated memory.",
    ),
    "Task5/calculate_gflops.c": (
        "8e2b87cd50540be797ca93a54440b6b681ebec69ca5ec6bf6650a74ead3af890",
        "Task 5 asks you to integrate your multiplication from Task 4 and to compute "
        "the time taken and the GFLOPS.",
    ),
}

SCREENSHOTS = {
    "t1.png": "Task 1: the Pi's terminal showing the output of `gcc --version`.",
    "t3_2c.png": "Task 3.2 c): the stack's memory bytes in gdb, showing the buffer overflow.",
    "t3_3.png": "Task 3.3: the output of your `foo` program.",
    "t5_rpi.png": "Task 5: your GFLOPS plot for the Raspberry Pi.",
    "t5_local.png": "Task 5: your GFLOPS plot for your own machine.",
}

# `TODO:` at the start of a line or at the start of a markdown table cell,
# ignoring any occurrence inside an inline `code span`.
CODE_SPAN = re.compile(r"`[^`]*`")
TODO = re.compile(r"(?:^|\|)\s*TODO:")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


class Report:
    def __init__(self) -> None:
        self.problems: list[tuple[str, str]] = []
        self.notes: list[str] = []

    def fail(self, what: str, detail: str) -> None:
        self.problems.append((what, detail))

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    @property
    def ok(self) -> bool:
        return not self.problems


def find_todos(text: str) -> list[tuple[int, str]]:
    """Return (line number, enclosing heading) for every unfilled slot."""
    hits: list[tuple[int, str]] = []
    heading = "(top of file)"
    for n, raw in enumerate(text.splitlines(), start=1):
        m = HEADING.match(raw.strip())
        if m:
            heading = m.group(2).strip()
            continue
        if TODO.search(CODE_SPAN.sub("", raw)):
            hits.append((n, heading))
    return hits


def section_body(text: str, heading_substring: str) -> str:
    """Text between the heading containing `heading_substring` and the next heading."""
    lines = text.splitlines()
    start = None
    level = 0
    for i, raw in enumerate(lines):
        m = HEADING.match(raw.strip())
        if m and heading_substring.lower() in m.group(2).lower():
            start, level = i + 1, len(m.group(1))
            break
    if start is None:
        return ""
    out = []
    for raw in lines[start:]:
        m = HEADING.match(raw.strip())
        if m and len(m.group(1)) <= level:
            break
        out.append(raw)
    return "\n".join(out)


def table_value(section: str, field: str) -> str | None:
    """Value cell of a `| field | value |` row, or None if it is still blank."""
    m = re.search(r"^\|\s*" + re.escape(field) + r"[^|]*\|([^|]*)\|", section, re.M)
    if not m:
        return None
    value = m.group(1).strip()
    return None if not value or value.startswith("TODO:") else value


def check_report(r: Report) -> str | None:
    path = ROOT / "REPORT.md"
    if not path.exists():
        r.fail("REPORT.md", "File is missing -- it must not be renamed or deleted.")
        return None

    text = path.read_text(encoding="utf-8")
    todos = find_todos(text)
    if todos:
        by_section: dict[str, list[int]] = {}
        for line, heading in todos:
            by_section.setdefault(heading, []).append(line)
        detail = "\n".join(
            f"  - **{heading}** — line(s) {', '.join(str(n) for n in lines)}"
            for heading, lines in by_section.items()
        )
        r.fail(
            "REPORT.md",
            f"{len(todos)} unanswered slot(s) still contain `TODO:`:\n{detail}",
        )

    team = section_body(text, "Team & process")
    group = table_value(team, "Group number")
    for field in ("Team member 1", "Team member 2"):
        if not table_value(team, field):
            r.fail(
                "REPORT.md",
                f"**{field}** is empty. You work in a group of two, so both names belong in "
                "the table at the top -- also if your partner did not touch the repository.",
            )
    if not group:
        r.fail("REPORT.md", "**Group number** is empty. Use the number from Canvas.")
    elif not re.fullmatch(r"\d+", group):
        r.fail(
            "REPORT.md",
            f"**Group number** is `{group}` -- please write digits only, e.g. `7`.",
        )
    return group


def check_repo_name(r: Report, group: str | None) -> None:
    """The repo name is how we match a hand-in to a group.

    This only ever warns: a freshly created repository is allowed to be red for the
    right reasons (unanswered questions), not for its name.
    """
    slug = os.environ.get("GITHUB_REPOSITORY", "")
    if not slug:
        return  # running locally; nothing to check against
    name = slug.split("/")[-1]
    if name == TEMPLATE_REPO:
        return  # this is the template itself, not a hand-in

    m = re.search(r"group0*(\d+)", name, re.I)
    if not m or not name.lower().startswith("ics-a3"):
        r.note(
            f"⚠️ **Please rename this repository.** It is called `{name}`, but it has to be "
            f"`{REPO_PREFIX}<your number>` — digits only, e.g. `{REPO_PREFIX}7` — so we can "
            "match it to your group. Do it under **Settings → General → Repository name**; "
            "links to the old name keep working, so it is safe to rename at any time."
        )
    elif group and m.group(1) != group.lstrip("0"):
        r.note(
            f"The repository is named `{name}` but `REPORT.md` says group **{group}**. "
            "One of the two is wrong -- please make them agree."
        )


def check_screenshots(r: Report) -> None:
    for name, what in SCREENSHOTS.items():
        rel = f"screenshots/{name}"
        path = ROOT / "screenshots" / name
        if not path.exists():
            r.fail(rel, f"Missing. {what} The file name has to match exactly.")
        elif path.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            r.fail(
                rel,
                "File is not a real PNG. Renaming a .jpg to .png does not convert it -- "
                "export it as PNG instead.",
            )


def strip_c(src: str) -> str:
    """C source without comments and whitespace, so leftover comments don't count as work."""
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"//[^\n]*", "", src)
    return re.sub(r"\s+", "", src)


def fingerprint(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    return hashlib.sha256(strip_c(text).encode("utf-8")).hexdigest()


def check_code(r: Report) -> None:
    for name, (starter, task) in STARTERS.items():
        path = ROOT / name
        if not path.exists():
            r.fail(name, f"File is missing. {task}")
        elif fingerprint(path) == starter:
            r.fail(name, f"Still the starting file we gave you. {task}")

    # A reminder, not a failure: there is more than one way to write this.
    matrix = ROOT / "Task4" / "matrix_multiplication.c"
    if matrix.exists() and fingerprint(matrix) != STARTERS["Task4/matrix_multiplication.c"][0]:
        code = strip_c(matrix.read_text(encoding="utf-8", errors="replace"))
        if not re.search(r"\b(malloc|calloc|realloc)\(", code):
            r.note(
                "`Task4/matrix_multiplication.c` does not seem to call `malloc`, `calloc` or "
                "`realloc`. Task 4 asks for memory that is allocated **at run time**."
            )


def main() -> int:
    if "--fingerprints" in sys.argv[1:]:
        for name in STARTERS:
            print(f"{fingerprint(ROOT / name)}  {name}")
        return 0

    r = Report()
    group = check_report(r)
    check_repo_name(r, group)
    check_screenshots(r)
    check_code(r)

    graders = " and ".join(f"`{g}`" for g in GRADERS)
    lines: list[str] = ["# Assignment 3 — submission check", ""]
    if r.ok:
        lines += [
            "✅ **Your hand-in looks complete.**", "",
            "This only checks that nothing is *missing* — it says nothing about whether "
            "your answers are right.", "",
            f"Before the deadline: make sure your partner, {graders} are collaborators "
            "here, and that **one** of you submits the repository URL on Canvas.",
        ]
    else:
        lines += [f"❌ **{len(r.problems)} thing(s) still to do.**", ""]
        for what, detail in r.problems:
            lines += [f"### `{what}`", "", detail, ""]

    if r.notes:
        # Leading "" matters: a `---` directly under text makes it a Markdown heading.
        lines += ["", "---", "", "### Notes", ""] + [f"- {n}" for n in r.notes]

    out = "\n".join(lines)
    print(out)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        Path(summary).write_text(out, encoding="utf-8")
    return 0 if r.ok else 1


if __name__ == "__main__":
    sys.exit(main())
