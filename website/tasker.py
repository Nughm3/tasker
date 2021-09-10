from datetime import datetime

# Basic greeting function based on the current time
def greet() -> str:
    now = int(datetime.now().strftime("%H"))
    if 0 <= now <= 6: greeting = "night"
    elif 7 <= now <= 11: greeting = "morning"
    elif 12 <= now <= 16: greeting = "afternoon"
    elif 17 <= now <= 20: greeting = "evening"
    else: greeting = "night"
    
    return greeting

class Task():
    def __init__(self, name, info, date, folder) -> None:
        self.name = name
        self.description = info
        self.due_date = date
        self.folder = folder
