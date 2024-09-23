# 🔬 Cryptography Benchmarking

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Cryptography Benchmarking](#-cryptography-benchmarking)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date. You can also
find the deadline for the project, as reported by GitHub Classroom, by clicking
the grey box at the top of this file. Please furthermore note that the content
provided in the `README.md` file for this GitHub repository is an overview of
the project and thus may not include the details for every step needed to
successfully complete every project deliverable. This means that you may need to
schedule a meeting during the course instructor's office hours to discuss
aspects of this project. Finally, it is important to point out that your
repository for this project was created from the GitHub repository template
called
[cryptography-benchmarking-starter](https://github.com/SecuritySynapse/cryptography-benchmarking-starter);
you can check this repository for any updates to this project's documentation or
source code!

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

This project invites you to implement and use a program called `cryptobenchmark`
that conducts a performance evaluation benchmarking campaign to automatically
measures the **time and memory overhead** of the following configurations:

- **Algorithm**:
  - *Standard*: `Fernet` from the `cryptography` library
  - *Rust-Based*: `rFernet` from the `rfernet` library
- **Mode**:
  - *Encryption*: `encrypt` function from either library
  - *Decryption*: `decrypt` from either library
- **Starting Text Size**:
  - *Small*: 256 characters
  - *Medium*: 512 characters
  - *Large*: 1024 characters
- **Doubling Rounds**:
  - *Small*: 10 rounds
  - *Medium*: 20 rounds
  - *Large*: 40 rounds

Whenever possible, you should conduct a doubling experiment with the
`cryptobenchmark` program by repeatedly doubling the size of the randomly
generated text-based input for the specified number of rounds and with the
stated starting text size in characters. This will enable you to measure the
time and memory overhead of the specified cryptographic algorithm and mode as
the size of the input text doubles, ultimately revealing the likely worst-case
time complexity of the specified algorithm and mode.

Running a command like `poetry run cryptobenchmark --textsize 256 --mode decrypt
--library fernet --doublerounds 10` will run the `cryptobenchmark` program with
a specified set of configuration and ultimately produce output like the
following:

```text
🏃 Performing a benchmarking campaign with cryptography algorithms!
💥 Should the benchmarking campaign produce verbose output? False
💥 The size of the text to be encrypted is: 256
💥 The number of doubling rounds is: 10
💥 The mode for the benchmarking campaign is: decrypt

Running a benchmark for text size: 256
Running a benchmark for text size: 512
Running a benchmark for text size: 1024
Running a benchmark for text size: 2048
Running a benchmark for text size: 4096
Running a benchmark for text size: 8192
Running a benchmark for text size: 16384
Running a benchmark for text size: 32768
Running a benchmark for text size: 65536
Running a benchmark for text size: 131072

📈 Performance Benchmark Results for Encryption

┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Text Size ┃ Time Overhead (s) ┃ Memory Overhead - Current (MiB) ┃ Memory Overhead - Peak (MiB) ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│       256 │           0.00011 │                         0.00028 │                      0.00239 │
│       512 │           0.00008 │                         0.00053 │                      0.00305 │
│      1024 │           0.00008 │                         0.00102 │                      0.00498 │
│      2048 │           0.00008 │                         0.00199 │                      0.00885 │
│      4096 │           0.00009 │                         0.00395 │                      0.01664 │
│      8192 │           0.00012 │                         0.00785 │                      0.03227 │
│     16384 │           0.00014 │                         0.01566 │                      0.06350 │
│     32768 │           0.00019 │                         0.03129 │                      0.12596 │
│     65536 │           0.00029 │                         0.06254 │                      0.25094 │
│    131072 │           0.00052 │                         0.12504 │                      0.50092 │
└───────────┴───────────────────┴─────────────────────────────────┴──────────────────────────────┘
```

As you can see in the output of the `cryptobenchmark` program, the final data
table must contain the following columns: `Text Size`, `Time Overhead (s)`,
`Memory Overhead - Current (MiB)`, and `Memory Overhead - Peak (MiB)`. Your
program should measure the time overhead in seconds using the `time` package and
measure the `current` and `peak` memory overhead in MiB using the `tracemalloc`
and/or `memory_profiler` packages. All of the data inside of the output table
should be right-aligned and formatted to a consistent number of decimal places.
Finally, the `cryptobenchmark` program should display diagnostic information
about, for instance, the command-line arguments and the details about each round
of input-size doubling. When conducting your experiment, if it is not possible
to run the `cryptobenchmark` program with the specified configuration due to,
for instance, memory or CPU limitations, then you should document and explain
these details in the `writing/reflection.md` file. Although it is not explicitly
evident in the output, your program must also contain checks, encoded in form of
assertions that use the `assert` keyword, that verify that the round-trip use of
the cryptographic algorithms worked correctly.

After cloning this repository to your computer, please take the following steps
to get started on the project:

- Make sure that you are using a recent version of Python 3.12 to complete this
assignment by typing `python --version` in your terminal; if you are not using
a recent version of Python please upgrade before proceeding.
- Make sure that you are using a recent version of Poetry 1.8 to complete this
assignment by typing `poetry --version` in your terminal; if you are not using
a recent version of Poetry please upgrade before proceeding.
- Before moving to the next step, you may need to again type `poetry install`
one or more times in order to avoid the appearance of warnings when you next
run the `cryptobenchmark` program. Note that you need to provide a complete
implementation of all of the `cryptobenchmark` program's features before you can
conduct your own benchmarking campaign to automatically conduct a performance
evaluation experiment using a doubling campaign.
- Since the `rfernet` library uses the Rust programming language in an attempt
to gain performance improvements, you will need to make sure that you have a
Rusts toolchain installed on your laptop that can use programs like `cargo` and
`rustc` to compile Rust programs.

Finally, here are other issues that you should keep in mind as you work on the
`cryptobenchmark` program:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical
writing prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker
and the entire prompt and then add your own comments to demonstrate that you
understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
