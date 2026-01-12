# Project 1  Log Parser

The script reads a log file then counts the entry's (INFO,WARNING,ERROR) then to filter the logs by user specified levels to generate a report where it print the first and last timestamps, and saves parsed data to a file which can be further reviewed.

# How to use it

python main.py

This prompt in the terminal will prompt the user (you) for a log level to filter to  (INFO,WARNING,ERROR).
And make sure that your log file is inside of the Sample_logs folder.

# What I learned

I learnt how to read and write files in python with the use of open()
using counters, loops as well as conditionals to summarise data.
And having to handle edgde cases for empty log files.

# Technical Details

Language: Python
Key concepts: loops, conditionals, file I/O, string parsing, lists, dictionaries, timestamp generation, directory handling and reporting


# Below is an example of an OUTPUT.

Total number of entries: 5
First entry: hello
Last entry: WARNING

1: [2026-01-11 17:45:12] hello
2: [2026-01-11 17:45:12] cap
3: [2026-01-11 17:45:12] running
4: [2026-01-11 17:45:12] ERROR
5: [2026-01-11 17:45:12] WARNING

Info entries: 2
Warning entries: 1
Error entries: 1

Filtered logs for ERROR:
4: [2026-01-11 17:45:12] ERROR

Summary saved to Output/total_report.txt
