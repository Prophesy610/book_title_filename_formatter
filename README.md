# Book Title Filename Formatter

This script automatically corrects and standardizes filenames in a directory to follow proper book title grammar rules. It is designed to help organize collections of book files, making them easier to sort and search for.

## Features

- **Grammar-based renaming:** Converts filenames to proper book title casing, handling common punctuation and word capitalization rules.
- **Batch processing:** Corrects multiple files in a directory at once.
- **Flexible:** Supports a variety of file extensions (e.g., `.pdf`, `.epub`, `.mobi`, etc.).
- **Simple to use:** Easy command-line interface with minimal setup.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/book_title_filename_formatter.git
   cd book_title_filename_formatter

Ensure you have Python 3.x installed.

Install dependencies:

    pip install -r requirements.txt

## Usage

1. Place Your Files

    Move the files you want to rename into the desired directory. The script will process all files in the directory.

2. Run the Script

    Use the following command to run the script:

  ```bash
  python format_filenames.py /path/to/your/directory
  ```

Replace /path/to/your/directory with the actual path to your directory containing the files.

3. Review the Changes

    The script will display the old and new filenames in the terminal. If everything looks correct, you can confirm the changes. The filenames will be updated automatically according to proper title capitalization rules.

## Example

### Before:

the_wind_in_the_willows.pdf

to_kill_a_mockingbird.epub

1984_by_george_orwell.mobi

### After:

The Wind in the Willows.pdf

To Kill a Mockingbird.epub

1984 by George Orwell.mobi


## Title Grammar Rules

The script applies the following book title grammar rules:

- Capitalize major words:** First and last words are always capitalized, along with any word that is not an article, preposition, or conjunction.
- Lowercase articles, prepositions, and conjunctions:** Articles like "the," "a," "an" and conjunctions like "and," "but" will be converted to lowercase unless they are at the start or end of the title.
- Keep punctuation intact:** Commas, periods, colons, etc., are retained in the filename.


## Configuration

If you need to fine-tune the script to handle specific edge cases, you can modify the format_filenames.py file. Feel free to open an issue if you encounter problems or need further customizations!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

We welcome contributions! If you have suggestions, improvements, or bug fixes, feel free to fork the repository and submit a pull request.
