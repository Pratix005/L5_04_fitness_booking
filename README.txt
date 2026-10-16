Lab 5 submission bundle.
Contains the corrected gym_system.py, issue log, reflection answers, final report files, and Word report.
Note: The report text files summarize the final results shown in the terminal screenshots. For strict reproducibility, rerun the commands locally to regenerate native tool reports.
Commands:
python -m pylint gym_system.py > pylint_report.txt
python -m bandit -r gym_system.py --format txt 2> bandit_stderr.txt | Out-File -Encoding utf8 bandit_report.txt
python -m flake8 gym_system.py > flake8_report.txt
