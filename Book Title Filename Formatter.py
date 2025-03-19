import os
import re

# List of title case exceptions (words that should remain lowercase in titles)
TITLE_CASE_EXCEPTIONS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "nor", "of", "on", "or", "so", "the", "to", "up", "yet", "with"
}

def replace_special_chars(filename):
    """Replace special characters like underscores, hyphens, and periods (excluding file extensions)."""
    # Split filename and extension (to handle them separately)
    name, ext = os.path.splitext(filename)
    
    # Replace underscores and hyphens with spaces in the name part of the filename
    name = name.replace('_', ' ')  # Replace underscores with spaces
    name = name.replace('-', ' ')  # Replace hyphens with spaces
    
    # After replacing, join the name with the extension again
    return name + ext

def capitalize_title(filename):
    """Properly capitalize the filename as if it were a book title."""
    # Split the filename into words
    words = filename.split()

    # Capitalize the first and last word, and capitalize important words
    for i, word in enumerate(words):
        # If the word is in our exceptions list, make it lowercase
        if i != 0 and i != len(words) - 1 and word.lower() in TITLE_CASE_EXCEPTIONS:
            words[i] = word.lower()  # Make exceptions lowercase
        else:
            words[i] = word.capitalize()  # Capitalize other words

    return ' '.join(words)

def process_folder(folder_path):
    """Process all files in the given folder and subfolders."""
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # Get the full path of the file
            file_path = os.path.join(root, filename)

            # Process the filename: replace special characters and capitalize it
            new_filename = replace_special_chars(filename)
            new_filename = capitalize_title(new_filename)

            # If the filename has changed, rename the file
            if new_filename != filename:
                new_file_path = os.path.join(root, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")

def main():
    # Ask for the folder path (drag and drop the folder into the terminal)
    folder_path = input("Drag and drop the folder here: ").strip()

    # Remove extra escape characters (e.g., the backslashes)
    folder_path = folder_path.replace("\\", "")

    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory. Please check the path and try again.")
        return

    # Process the folder and all its subfolders
    process_folder(folder_path)

if __name__ == "__main__":
    main()
