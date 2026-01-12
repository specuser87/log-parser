
import os

def save_logs_to_file(logs, output_folder="Output", filename="auth_output.log"):
    """
    Save a list of logs to a file inside the output folder.
    Creates the folder if it doesn't exist.
    """
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    output_file = os.path.join(output_folder, filename)
    with open(output_file, "w") as f:
        for index, log in enumerate(logs, start=1):
            f.write(f"{index}: {log}\n")

    print(f"Log data successfully saved to {output_file}")
    return output_file


# ---------- Usage Example ----------
if __name__ == "__main__":
    from Activity1_loadfile import load_logs

    stored_logs = load_logs("Sample_Logs/auth.log")
    save_logs_to_file(stored_logs)
