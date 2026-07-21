total_items = 53
items_per_page = 10
full_pages, remaining_items = divmod(total_items, items_per_page)
print(f"Total full pages: {full_pages}")
print(f"Items on the last page: {remaining_items}")