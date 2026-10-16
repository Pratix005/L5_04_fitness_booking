# Lab 5 — Static Code Analysis: Issue Log

Repository: `SETAPESU26/L5_04_fitness_booking`  
Analyzed file: `gym_system.py`

| Issue | Type | Original line(s) | Finding and impact | Fix applied |
|---|---|---:|---|---|
| Dangerous shell execution | Security | 36 | Bandit B605: os.system() invoked a shell command using a constructed string; this also failed on Windows because `rm` is not a Windows command. | Replaced shell execution with pathlib.Path.glob(), is_file(), and unlink() to remove matching old_*.json files. |
| Mutable default argument | Bug / maintainability | 8 | A default list could be shared across function calls. | Changed attendance_log=[] to attendance_log=None and initialized a new list inside the function. |
| Bare exception | Reliability | 21 | A bare except could hide unrelated errors. | Caught the specific KeyError and ValueError exceptions expected from the cancellation operation. |
| Function naming style | Style | 27 | addMembers did not follow snake_case naming convention. | Renamed the function to add_members and updated its call sites. |
| File encoding and resource management | Maintainability | 32 | open() did not explicitly specify an encoding or use a context manager. | Used `with open(..., encoding='utf-8')` to ensure proper encoding and automatic file closure. |
| Missing documentation | Maintainability | 1, 8, 18, 24, 27, 31, 35, 38, 42 (original findings) | Pylint reported missing module/function docstrings. | Added a module docstring and descriptive docstrings for functions. |
| Formatting violations | Style | Multiple | Flake8 reported blank-line and exception-formatting violations in the original file. | Adjusted spacing and exception handling to comply with Flake8. |
| String formatting | Style / readability | 15 | Pylint recommended f-string formatting instead of percent-formatting. | Changed the attendance log entry to an f-string. |

## Verification summary

- **Pylint:** Final score 10.00/10 (observed in the terminal).
- **Bandit:** `No issues identified.` (observed in the final report).
- **Flake8:** Empty report; no style violations were printed.
- **Execution:** The corrected program ran on Windows without the original `rm is not recognized` message.

Line numbers above refer to the original version where findings were reported; line numbers may change after edits.
