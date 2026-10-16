"""Manage fitness class bookings, capacity, and roster exports."""

import json
from pathlib import Path


class_capacity = {"Yoga": 3, "HIIT": 2, "Spin": 4}
rosters = {}


def book_class(member_id, class_name, attendance_log=None):
    """Book a member into a class if capacity permits."""
    if attendance_log is None:
        attendance_log = []

    if class_name not in rosters:
        rosters[class_name] = []

    if len(rosters[class_name]) >= class_capacity.get(class_name, 0):
        print(f"Class full: {class_name}")
        return False

    rosters[class_name].append(member_id)
    attendance_log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id, class_name):
    """Cancel a member's booking when it exists."""
    try:
        rosters[class_name].remove(member_id)
    except (KeyError, ValueError):
        print("Nothing to cancel")


def set_capacity(class_name, seats):
    """Set the capacity for a fitness class."""
    if seats < 0:
        raise ValueError("Class capacity cannot be negative")
    class_capacity[class_name] = seats


def add_members(class_name, count):
    """Add the requested number of guest members."""
    if count < 0:
        raise ValueError("Guest count cannot be negative")

    for i in range(count):
        book_class(f"GUEST-{i}", class_name)


def export_roster(file="gym_schedule.json"):
    """Export the current rosters as JSON."""
    with open(file, "w", encoding="utf-8") as roster_file:
        json.dump(rosters, roster_file, indent=2)


def clear_old_exports(prefix="old_"):
    """Remove old JSON exports matching the supplied filename prefix."""
    for path in Path(".").glob(f"{prefix}*.json"):
        if path.is_file():
            path.unlink()


def show_rosters():
    """Display all current class rosters."""
    for class_name, members in rosters.items():
        print(f"{class_name}: {', '.join(str(member) for member in members)}")


def main():
    """Run the fitness booking demonstration."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class(55, "HIIT")
    book_class("M5", "Pilates")
    set_capacity("Spin", 4)
    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    guest_input = input("How many walk-in guests for HIIT? (Enter for 1): ")
    try:
        guest_count = int(guest_input) if guest_input.strip() else 1
        add_members("HIIT", guest_count)
    except ValueError:
        print("Please enter a valid non-negative integer.")
        return

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
