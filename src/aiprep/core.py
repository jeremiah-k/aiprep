"""Core functionality for the aiprep package."""

import glob
import os
import subprocess


def combine_files(file_list):
    """
    Combine multiple files into a single formatted string.

    Args:
        file_list (list): List of file paths to combine.

    Returns:
        str: Combined content with filenames and code blocks.
    """
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
    """
    Replace triple backticks with double backticks in a file.

    Args:
        file_path (str): Path to the file to modify.
    """
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
    """
    Replace double backticks with triple backticks in a file.

    Args:
        file_path (str): Path to the file to modify.
    """
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
    """
    Copy content to the system clipboard.

    Args:
        content (str): Content to copy to clipboard.
    """
    process = subprocess.Popen(
        ["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE
    )
    process.communicate(input=content.encode("utf-8"))


def recursive_glob(pattern):
    """
    Recursively find files matching a pattern.

    Args:
        pattern (str): Glob pattern to match.

    Returns:
        list: List of file paths matching the pattern.
    """
    return [y for x in os.walk(".") for y in glob.glob(os.path.join(x[0], pattern))]
