#!/usr/bin/env python3
import os
import subprocess
import sys

def combine_files(file_list):
    combined_content = []
    for file_path in file_list:
        if not os.path.isfile(file_path):
            print(f"Warning: {file_path} is not a valid file. Skipping.")
            continue
        combined_content.append(f"{file_path}:\n```")
        with open(file_path, "r") as f:
            combined_content.append(f.read())
        combined_content.append("```\n")
    return "\n".join(combined_content)

def deblock_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file.")
        return
    with open(file_path, "r") as f:
        content = f.read()
    updated_content = content.replace("```", "``")
    with open(file_path, "w") as f:
        f.write(updated_content)
    print(f"Updated {file_path}: triple backticks changed to double backticks.")

def reblock_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file.")
        return
    with open(file_path, "r") as f:
        content = f.read()
    updated_content = content.replace("``", "```")
    with open(file_path, "w") as f:
        f.write(updated_content)
    print(f"Updated {file_path}: double backticks changed to triple backticks.")

def copy_to_clipboard(content):
    process = subprocess.Popen(
        ["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE
    )
    process.communicate(input=content.encode("utf-8"))

def print_help():
    print("""Usage: aiprep.py [OPTIONS] <file1> <file2> ... <fileN>
Options:
  --help         Show this help message and exit.
  -c             Combine the content of files into a clipboard-friendly format with codeblocks.
  --db           Change all triple backticks (```) to double backticks (``) in the specified files.
  --rb           Change all double backticks (``) to triple backticks (```) in the specified files.
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    option = sys.argv[1]
    files = sys.argv[2:]

    if option == "--help":
        print_help()
    elif option == "-c":
        if not files:
            print("Error: No files provided for combining.")
            sys.exit(1)
        combined_content = combine_files(files)
        copy_to_clipboard(combined_content)
        print("Combined content copied to clipboard.")
    elif option == "--db":
        if not files:
            print("Error: No files provided for deblocking.")
            sys.exit(1)
        for file in files:
            deblock_file(file)
    elif option == "--rb":
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
