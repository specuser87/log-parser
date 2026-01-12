import os
from datetime import datetime

stored_logs = []

log_file = "Sample_Logs/auth.log"

if not os.path.exists(log_file) or os.path.getsize(log_file) == 0:
    print("Log file missing or empty")
    exit()

with open(log_file, "r") as file:
    stored_logs = [line.strip() for line in file]

print("The total number of entries is:", len(stored_logs))
print("Your first entry in the log file is:", stored_logs[0])
print("Your last entry is:", stored_logs[-1])

first_timestamp = None
last_timestamp = None

for index, log in enumerate(stored_logs, start=1):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if first_timestamp is None:
        first_timestamp = timestamp
    last_timestamp = timestamp
    print(f"{index}: [{timestamp}] {log}")

INFO_count = 0
WARNING_count = 0
ERROR_count = 0

for log in stored_logs:
    if "INFO" in log:
        INFO_count += 1
    elif "WARNING" in log:
        WARNING_count += 1
    elif "ERROR" in log:
        ERROR_count += 1

print(f"INFO entries:", INFO_count)
print(f"WARNING entries:", WARNING_count)
print(f"ERROR entries:", ERROR_count)

user = input("Enter a log level (INFO/WARNING/ERROR):").strip().upper()
filtered_list = [log for log in stored_logs if user in log]

if filtered_list:
    for entry in filtered_list:
        print(entry)
else:
    print("There are no log entries for this level")

output_folder = "Output"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

output_file = os.path.join(output_folder, "auth_output.log")
with open(output_file, "w") as file:
    for index, log in enumerate(stored_logs, start=1):
        file.write(f"{index}: {log}\n")

print("The log data has been successfully saved.")

total_entries = len(stored_logs)
first_timestamp = first_timestamp
last_timestamp = last_timestamp

print("\n----------- LOG SUMMARY REPORT -----------")
print(f"Total Log Entries: {total_entries}")
print(f"INFO entries:", INFO_count)
print(f"WARNING entries:", WARNING_count)
print(f"ERROR entries:", ERROR_count)
print(f"First timestamp:", first_timestamp)
print(f"Last timestamp:", last_timestamp)

report_file = os.path.join(output_folder, "total_report.txt")
with open(report_file, "w") as file:
    file.write("TOTAL LOG SUMMARY REPORT\n")
    file.write("------------------------\n")
    file.write(f"Total entries: {total_entries}\n")
    file.write(f"INFO entries: {INFO_count}\n")
    file.write(f"WARNING entries: {WARNING_count}\n")
    file.write(f"ERROR entries: {ERROR_count}\n")
    file.write(f"First timestamp: {first_timestamp}\n")
    file.write(f"Last timestamp: {last_timestamp}\n")

print("Summary of the total report saved to Output/total_report.txt")
