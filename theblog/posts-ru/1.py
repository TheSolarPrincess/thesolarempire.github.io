import os
import re

def remove_matching_text(file_path, pattern):
    with open(file_path, 'r') as file:
        content = file.read()
    
    new_content, num_substitutions = re.subn(pattern, '', content, flags=re.DOTALL)
    
    if num_substitutions > 0:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Removed {num_substitutions} matches from {file_path}")
    else:
        print(f"No matches found in {file_path}")
    
    return num_substitutions

# Regular expression pattern to match (modify this as needed)
pattern = r'\!\[\[Больше Солнечной Империи\]\]'

# File extension to process (modify if you want to process different file types)
file_extension = '.md'

# Get all files with the specified extension in the current directory
target_files = [f for f in os.listdir('.') if f.endswith(file_extension)]

total_files = len(target_files)
files_modified = 0
total_matches_removed = 0

# Process each file
for file_name in target_files:
    matches_removed = remove_matching_text(file_name, pattern)
    if matches_removed > 0:
        files_modified += 1
        total_matches_removed += matches_removed

print(f"\nSummary:")
print(f"Total files processed: {total_files}")
print(f"Files modified: {files_modified}")
print(f"Total matches removed: {total_matches_removed}")