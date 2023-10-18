import datetime

def format_duration(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    formatted_duration = ""
    
    if days > 0:
        formatted_duration += f"{days}d "
    if hours > 0:
        formatted_duration += f"{hours}h "
    if minutes > 0:
        formatted_duration += f"{minutes}m "
    
    return formatted_duration.strip()

def calculate_duration(clock):
    timestamp = datetime.datetime.utcfromtimestamp(int(clock))
    current_time = datetime.datetime.utcnow()
    duration_seconds = (current_time - timestamp).total_seconds()
    return format_duration(int(duration_seconds))
