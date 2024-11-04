import os

# Define the line to check and the line to append
line_to_check = "[[The Solar Empire|Other posts]]"
line_to_append = "<div id=\"isso-thread\"></div>"

# Get the list of all .md files in the current directory
current_directory = os.getcwd()
md_files = [f for f in os.listdir(current_directory) if f.endswith('.md')]

# Process each .md file
for md_file in md_files:
    file_path = os.path.join(current_directory, md_file)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the line_to_check is present
    if any(line_to_check in line for line in lines):
        # If present, append the line_to_append
        with open(file_path, 'a') as file:
            file.write(line_to_append + '\n')
        print(f'Appended to {md_file}')

print('Script completed.')
