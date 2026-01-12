

def filter_logs_by_level(logs, level):
    """
    Filter logs for a specific level (INFO, WARNING, ERROR).
    
    Returns a list of filtered log entries.
    """
    level = level.upper()
    filtered = [log for log in logs if level in log]
    return filtered


# ---------- Usage Example ----------
if __name__ == "__main__":
    from CODE.Activity1_loadfile import load_logs

    stored_logs = load_logs("Sample_Logs/auth.log")
    user_level = input("Enter log level to filter (INFO/WARNING/ERROR): ").strip()
    filtered = filter_logs_by_level(stored_logs, user_level)

    if filtered:
        print(f"\nFiltered logs ({user_level}):")
        for log in filtered:
            print(log)
    else:
        print(f"No logs found for level: {user_level}")
