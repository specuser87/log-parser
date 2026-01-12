
from datetime import datetime

def display_logs(logs):
    """
    Display each log entry with a line number starting from 1.
    Optionally includes a timestamp of display.
    """
    first_timestamp = None
    last_timestamp = None

    for index, log in enumerate(logs, start=1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if first_timestamp is None:
            first_timestamp = timestamp
        last_timestamp = timestamp
        print(f"{index}: [{timestamp}] {log}")

    return first_timestamp, last_timestamp


# ---------- Usage Example ----------
if __name__ == "__main__":
    # Example usage if you run this file directly
    from CODE.Activity1_loadfile import load_logs

    log_file = "Sample_Logs/auth.log"
    stored_logs = load_logs(log_file)

    first_ts, last_ts = display_logs(stored_logs)
    print("\nFirst timestamp:", first_ts)
    print("Last timestamp:", last_ts)

