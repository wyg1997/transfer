import os
from os import path as osp
import tempfile
import zipfile
import base64


def compress_directory(directory):
    """
    Compress the directory in zip and return the compressed file.
    """
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as temp:
        # Create the zip file
        with zipfile.ZipFile(temp, "w") as zip_file:
            # Walk the directory and add the files to the zip file
            for root, _, files in os.walk(directory):
                for file in files:
                    zip_file.write(os.path.join(root, file))

        return temp.name


def check_gpg_install():
    """
    Check if gpg is installed.
    """
    # check gpg
    if os.system("gpg --version > /dev/null 2>&1") != 0:
        raise RuntimeError("gpg is not installed. Please install gpg firstly.")


def run_command_and_return(command: str):
    """
    Run the command and return the output.
    """
    return os.popen(command).read()


def write_string_to_clipboard(string: str):
    """
    Write the string to the clipboard.
    """

    def write_to_tty(data: bytes) -> None:
        with open("/dev/tty", "wb") as f:
            f.write(data)
            f.flush()

    base64_str = base64.b64encode(string.encode())
    osc52_str = b"\033]52;p;" + base64_str + b"\a"
    write_to_tty(osc52_str)


def read_text_from_file(file_path: str):
    """
    Read the string from the file.
    """
    if not osp.isfile(file_path):
        raise RuntimeError(f"{file_path} is not a file.")

    with open(file_path, "r") as f:
        return f.read()
