import os

def replace_in_file(file_path, old_string, new_string):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the old string with the new string
    new_content = content.replace(old_string, new_string)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def replace_in_md_files(directory, old_string, new_string):
    # Walk through the directory
    for dirpath, _, files in os.walk(directory):
        for file in files:
            # Check for .md files
            if file.endswith('.html'):
                file_path = os.path.join(dirpath, file)
                print(f'Processing: {file_path}')
                replace_in_file(file_path, old_string, new_string)

if __name__ == '__main__':
    # Set the directory, old string, and new string
    directory = "."
    old_string = "<div id=\"isso-thread\"></div>"
    new_string = """
    <div id="isso-thread"></div>
    <script 
        data-isso="https://violet-mire-cook.glitch.me"
        data-isso-css="true"
        data-isso-lang="en"
        data-isso-reply-to-self="false"
        data-isso-require-author="false"
        data-isso-require-email="false"
        src="https://thesolarprincess.github.io/tsp-cdn/inno.min.js">
    </script>
    """

    replace_in_md_files(directory, old_string, new_string)
    print("Replacement complete.")
