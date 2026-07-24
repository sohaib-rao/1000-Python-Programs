import os


def rename_item(old_name, new_name):
  os.rename(old_name, new_name)
  print(f"Successfully renamed '{old_name}' to '{new_name}'.")


old_name, new_name = (
    "222. finding floor and ceiling value.py",
    "222. finding floor & ceiling value.py",
)
rename_item(old_name, new_name)