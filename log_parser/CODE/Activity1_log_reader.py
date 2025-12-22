storedlist = []

file_path = "Sample_Logs/auth.log"

with open(file_path, "r") as file:
    for lines in file:
        storedlist.append(lines.strip())

        print("The total number of entries is: {storedlist}")
        print("The first entry is: {storedlist}[0]")
        print("The last entry is: {storedlist}[-1]")






