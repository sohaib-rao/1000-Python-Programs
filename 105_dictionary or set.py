import os

# Directory jahan files hain
directory = '.'

for filename in os.listdir(directory):
    # Sirf .py files ko touch karein
    if filename.endswith(".py"):
        # Purana format "001. filename.py" hai, toh usse split karte hain
        # Pehle dot (.) se split kiya
        parts = filename.split('.', 1)
        
        if len(parts) == 2 and parts[0].isdigit():
            number = parts[0] # Ye string format mein "001" hai
            rest_of_name = parts[1].strip() # Ye "filename.py" hai
            
            # Naya format: "001_filename.py"
            # Note: rest_of_name mein agar pehle se space hai toh usey strip kar rahe hain
            new_filename = f"{number}_{rest_of_name}"
            
            # Agar naam alag hai toh rename karein
            if filename != new_filename:
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} -> {new_filename}")