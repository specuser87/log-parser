storedlogs = []

open_log = 'Sample_Logs/auth.log' 

with open (open_log, 'r') as file:
    for line in file:
        storedlogs.append(line.strip)

print("The total number of entry's are: ", len(storedlogs))
print("The first entry is:",(storedlogs[0]))
print("The last entry's is:", (storedlogs[-1]))


for index, log in enumerate(storedlogs, start=1):
    print("{index}:{log}")


INFO = 0
WARNING = 0
ERROR = 0

for  log in storedlogs:
    if "INFO" in log:
     INFO +=1
    elif "WARNING"in log:
     WARNING +=1
    elif "ERROR" in log:
     ERROR += 1



user_level = input("Enter the log level (ERROR/ WARNING/ INFO)").strip().upper().lower()
# used upper and lower just in case if the user types in either lowercase or uppercase
filtered_logs = []

for log in storedlogs:
   if user_level in log:
      filtered_logs.append(log)

   else:
    print("There are no other valid log entry's for this level.")