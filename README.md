# aiprep.py

## Overview

The `aiprep.py` script allows you to easily combine multiple files into a single formatted output that can be loaded into an AI prompt. The combined content is copied to your clipboard, formatted with filenames and code block delimiters, making it easy to paste into AI tools or other text processors.

## Features

- Combines multiple files into a single output.
- Formats the output with filenames and backticks for code blocks.
- Copies the result to the clipboard for easy pasting.
- Skips invalid files with a warning.

## Installation

1. Ensure Python 3 is installed on your system.
2. Install `xclip` for clipboard functionality:

```bash
sudo apt-get install xclip
```

3. Download or clone the script into your preferred directory.
4. Make the script executable:

```bash
chmod +x aiprep.py
```

## Usage

Run the script from the terminal with the files you want to combine as arguments:

```bash
./aiprep.py <file1> <file2> ... <fileN>
```

### Example

```bash
./aiprep.py file1.py file2.py file3.py file4.py
```

### Expected Output (Copied to Clipboard)

The combined output will have the following format (with codeblocks intact):

```text
file1.py:
``
<contents of file1.py>
``

file2.py:
``
<contents of file2.py>
``

file3.py:
``
<contents of file3.py>
``

file4.py:
``
<contents of file4.py>
``
```

## Notes

- Ensure all specified files exist. Non-existent or invalid file paths will be skipped with a warning.
- You can modify the script to include additional formatting or functionality as needed.

## Purpose

This script is designed to streamline the process of loading multiple source code files into an AI prompt. By combining files into a single clipboard-ready format, it reduces the manual effort of copying and pasting each file individually.

## License

Feel free to use, modify, and distribute this script as needed. No restrictions apply.
