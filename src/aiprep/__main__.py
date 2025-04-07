"""Command-line interface for aiprep."""

import sys

from .core import (
    combine_files,
    copy_to_clipboard,
    deblock_file,
    reblock_file,
    recursive_glob,
)


def print_help():
    """Print usage instructions."""
    print(
        """Usage: aiprep [OPTIONS] <file1> <file2> ... <fileN>
Options:
  -h, --help            Show this help message and exit.
  -c, --combine         Combine the content of files into a clipboard-friendly format with codeblocks.
  -d, --deblock         Change all triple backticks (```) to double backticks (``) in the specified files.
  -r, --reblock         Change all double backticks (``) to triple backticks (```) in the specified files.
  --recursive           Recursively include files matching the given glob patterns.
"""
    )


def main():
    """Main entry point for the command-line interface."""
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    option = sys.argv[1]
    args = sys.argv[2:]

    recursive = False
    if "--recursive" in args:
        recursive = True
        args.remove("--recursive")

    files = list(args)

    if recursive and args:
        patterns = args
        for pattern in patterns:
            found = recursive_glob(pattern)
            files.extend(found)

    files = list(dict.fromkeys(files))

    if option in ("-h", "--help"):
        print_help()
    elif option in ("-c", "--combine"):
        if not files:
            print("Error: No files provided for combining.")
            sys.exit(1)
        combined_content = combine_files(files)
        copy_to_clipboard(combined_content)
        print("Combined content copied to clipboard.")
    elif option in ("-d", "--deblock"):
        if not files:
            print("Error: No files provided for deblocking.")
            sys.exit(1)
        for file in files:
            deblock_file(file)
    elif option in ("-r", "--reblock"):
        if not files:
            print("Error: No files provided for reblocking.")
            sys.exit(1)
        for file in files:
            reblock_file(file)
    else:
        print(f"Error: Unknown option '{option}'.")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
