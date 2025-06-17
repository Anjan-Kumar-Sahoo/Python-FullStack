from typing import List, Dict

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]
def structure_log(line: str) -> Dict:
    timestamp, level, user, message = line.split(" ",3)
    return {
        "timestamp": timestamp.strip("[]"),
        "level": level.strip(),
        "user": user.strip(":"),
        "message": message.strip()
    }

def add_log(self, line: str) -> None :
    logs.append(line)

def get_user_logs(self, user_id: str) -> List[Dict]:
    user_logs = []
    for log in logs:
        data = structure_log(log)
        if data.user == user_id:
            user_logs.append(data)
    return user_logs

def count_levels(self) -> Dict[str, int]:
    level_count = {}
    for log in logs:
        data = structure_log(log)
        level = data.level
        if level not in level_count:
            level_count[level] = 0
        level_count[level] += 1
    return level_count

def filter_logs(keyword: str) -> List[Dict]:
    filtered = []
    keyword_lower = keyword.lower()
    for log in logs:
        data = structure_log(log)
        if keyword_lower in data.message.lower():
            filtered.append(data)
    return filtered

def get_recent_logs(capacity: int = 5) -> List[Dict]:
    recent = []
    for log in logs[-capacity:]:
        data = structure_log(log)
        recent.append(data)
    return recent

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add Log")
        print("2. Get User Logs")
        print("3. Count Log Levels")
        print("4. Filter Logs by Keyword")
        print("5. Get Recent Logs")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            line = input("Enter log line (format: [timestamp] LEVEL user: message): ")
            add_log(line)
            print("Log added.")
        elif choice == "2":
            user_id = input("Enter user id (e.g., user1): ")
            user_logs = get_user_logs(user_id)
            for entry in user_logs:
                print(f"[{entry.timestamp}] {entry.level} {entry.user}: {entry.message}")
        elif choice == "3":
            counts = count_levels()
            print(counts)
        elif choice == "4":
            keyword = input("Enter keyword to filter: ")
            filtered = filter_logs(keyword)
            for entry in filtered:
                print(f"[{entry.timestamp}] {entry.level} {entry.user}: {entry.message}")
        elif choice == "5":
            recent = get_recent_logs()
            for entry in recent:
                print(f"[{entry.timestamp}] {entry.level} {entry.user}: {entry.message}")
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()