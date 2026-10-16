# Lab 5 — Static Code Analysis: Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues were style-related findings, such as blank-line spacing, f-string formatting, and renaming `addMembers` to `add_members`. These changes were localized and did not require changing the program's overall behavior. The hardest issue was the Bandit high-severity warning for shell execution in `clear_old_exports()`. The shell command was also incompatible with Windows. Replacing it with `pathlib` file operations required care so the cleanup remained limited to files matching the intended prefix and extension.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

No confirmed false positives were identified during this lab. The Bandit warning about `os.system()` was actionable: the code invoked a shell command assembled from a prefix, and the `rm` command failed in the Windows environment. The warning was addressed by replacing shell execution with Python file operations. A warning should only be called a false positive after checking the code and context, rather than simply because the program appears to run.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Flake8 and Pylint locally before committing changes, and run Bandit as part of the same check or in a continuous-integration pipeline. The CI pipeline could fail a pull request when new high-severity security findings or agreed-upon quality violations appear. I would review the reports, fix genuine findings, and document any justified exceptions instead of suppressing warnings without explanation.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The observed Pylint score increased from 6.60/10 to 10.00/10. Bandit changed from reporting one high-severity shell-execution issue to reporting no issues, and the final Flake8 report was empty. The code now uses a non-mutable default pattern, specific exception types, descriptive docstrings, UTF-8 file handling, a context manager, snake_case naming, and pathlib instead of a shell command. The program also ran on Windows without the original `rm` command error.
