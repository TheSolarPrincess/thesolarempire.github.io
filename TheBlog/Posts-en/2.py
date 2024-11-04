import os

# Define the line to remove
line_to_remove = "[Leave an anonymous comment](https://www.admonymous.co/thesolarprincess)"

# Get the list of all .md files in the current directory
current_directory = os.getcwd()
md_files = [f for f in os.listdir(current_directory) if f.endswith('.md')]

# Process each .md file
for md_file in md_files:
    file_path = os.path.join(current_directory, md_file)

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Filter out the line_to_remove
    new_lines = [line for line in lines if line.strip() != line_to_remove]
    
    # Write back the modified lines if any changes were made
    if len(new_lines) != len(lines):
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f'Removed line from {md_file}')

print('Script completed.')
