

def count_log_levels(logs):
    """
    Count the number of INFO, WARNING, and ERROR entries in the logs.
    
    Returns:
        info_count (int), warning_count (int), error_count (int)
    """
    info_count = 0
    warning_count = 0
    error_count = 0

    for log in logs:
        if "INFO" in log:
            info_count += 1
        elif "WARNING" in log:
            warning_count += 1
        elif "ERROR" in log:
            error_count += 1

    return info_count, warning_count, error_count


# ---------- Usage Example ----------
if __name__ == "__main__":
    from CODE.Activity1_loadfile import load_logs

    stored_logs = load_logs("Sample_Logs/auth.log")
    info, warning, error = count_log_levels(stored_logs)

    print(f"INFO entries: {info}")
    print(f"WARNING entries: {warning}")
    print(f"ERROR entries: {error}")
