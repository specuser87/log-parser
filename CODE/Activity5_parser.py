

def parse_logs_structured(logs):
    """
    Extract timestamp, level, and message from each log entry.
    Assumes logs are formatted like: [LEVEL] message
    Returns a list of dictionaries.
    """
    structured = []

    for log in logs:
        parts = log.split(" ", 1)  # split first word (level) from rest
        if len(parts) == 2:
            level, message = parts
        else:
            level = parts[0]
            message = ""
        structured.append({
            "level": level.strip(),
            "message": message.strip()
        })

    return structured


# ---------- Usage Example ----------
if __name__ == "__main__":
    from CODE.Activity1_loadfile import load_logs

    stored_logs = load_logs("Sample_Logs/auth.log")
    structured = parse_logs_structured(stored_logs)

    for entry in structured:
        print(entry)
