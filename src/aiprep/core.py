"""Core functionality for the aiprep package."""

import glob
import os

import pyperclip


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
    try:
        pyperclip.copy(content)
    except pyperclip.PyperclipException as e:
        print(f"Error copying to clipboard: {e}")


def recursive_glob(pattern):
    return [y for x in os.walk(".") for y in glob.glob(os.path.join(x[0], pattern))]
