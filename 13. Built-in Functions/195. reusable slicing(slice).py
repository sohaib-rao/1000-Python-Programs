# slice() creates a reusable slice object to extract specific parts of sequences
log_entry = "2026-07-21 ERROR Connection timed out"

# Extracting data using standard slice notation indices (start, stop)
date_slice = slice(0, 10)
level_slice = slice(11, 16)
message_slice = slice(17, None)

print(f"Date: {log_entry[date_slice]}")
print(f"Level: {log_entry[level_slice]}")
print(f"Message: {log_entry[message_slice]}")