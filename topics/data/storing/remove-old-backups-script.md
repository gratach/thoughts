# Remove old backups script

This backup script removes old backups from a directory `BACKUP_DIR`. It keeps a total of `MAX_BACKUPS` backups that are distributed over an interval starting from a date saved in `FIRST_BACKUP_FILE` ending at the current time. More recent dates have a higher priority.
Currently increasing `MAX_BACKUPS` only has an effect of additionally keeping more recent backups and not older ones.

This script is used in [in the Nextcloud configuration manual](../../linux/hosting/host-a-nextcloud-server.md).

```
#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path

# Configuration
BACKUP_DIR = Path("/var/backups")
FIRST_BACKUP_FILE = BACKUP_DIR / "first-backup-date.txt"
MAX_BACKUPS = 20

BACKUP_TIME_FORMAT = "%Y-%m-%d-%H-%M"


def load_first_backup_time():
    with open(FIRST_BACKUP_FILE, "r") as f:
        return datetime.strptime(
            f.read().strip(),
            BACKUP_TIME_FORMAT
        )


def load_backups():
    backups = []

    for entry in BACKUP_DIR.glob("*.tar.gz"):
        timestamp = entry.name.removesuffix(".tar.gz")

        try:
            backup_time = datetime.strptime(
                timestamp,
                BACKUP_TIME_FORMAT
            )
            backups.append((entry, backup_time))
        except ValueError:
            continue

    backups.sort(key=lambda x: x[1])
    return backups


def generate_target_points(first_backup_time, now, count):
    if count <= 0:
        return []

    points = [now]

    if count == 1:
        return points

    second = first_backup_time + (now - first_backup_time) / 2
    points.append(second)

    while len(points) < count:
        previous = points[-1]
        points.append(
            previous + (now - previous) / 2
        )

    return points


def select_backups(backups, target_points):
    available = list(backups)
    selected = []

    for point in target_points:
        if not available:
            break

        nearest = min(
            available,
            key=lambda backup: abs(
                (backup[1] - point).total_seconds()
            )
        )

        selected.append(nearest)
        available.remove(nearest)

    return selected


def main():
    first_backup_time = load_first_backup_time()
    now = datetime.now()

    backups = load_backups()

    if len(backups) <= MAX_BACKUPS:
        print(
            f"{len(backups)} backups found, "
            "nothing to delete."
        )
        return

    target_points = generate_target_points(
        first_backup_time,
        now,
        MAX_BACKUPS
    )

    selected = select_backups(
        backups,
        target_points
    )

    selected_files = {
        backup[0]
        for backup in selected
    }

    print("Keeping:")
    for backup_file, backup_time in sorted(
        selected,
        key=lambda x: x[1]
    ):
        print(f"  {backup_file.name}")

    print("\nDeleting:")

    deleted_count = 0

    for backup_file, backup_time in backups:
        if backup_file in selected_files:
            continue

        print(f"  {backup_file.name}")
        backup_file.unlink()
        deleted_count += 1

    print(
        f"\nFinished. "
        f"Kept {len(selected_files)} backups, "
        f"deleted {deleted_count}."
    )


if __name__ == "__main__":
    main()
```