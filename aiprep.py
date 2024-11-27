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


def copy_to_clipboard(content):
    process = subprocess.Popen(
        ["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE
    )
    process.communicate(input=content.encode("utf-8"))


def main():
    if len(sys.argv) < 2:
        print("Usage: aiprep.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    file_list = sys.argv[1:]
    combined_content = combine_files(file_list)
    copy_to_clipboard(combined_content)
    print("Combined content copied to clipboard.")


if __name__ == "__main__":
    main()
