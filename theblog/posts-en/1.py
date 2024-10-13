import os

# Text to append to each file
text_to_append = """
[[The Solar Empire|Other posts]]
[Leave an anonymous comment](https://www.admonymous.co/thesolarprincess) 
"""

# Get all .md files in the current directory
md_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Append the text to each file
for file_name in md_files:
    with open(file_name, 'a') as file:
        file.write(text_to_append)
    print(f"Appended text to {file_name}")

print(f"Finished appending text to {len(md_files)} files.")