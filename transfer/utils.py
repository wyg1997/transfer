import os
import tempfile
import zipfile


def compress_directory(directory):
    """
    Compress the directory in zip and return the compressed file.
    """
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as temp:
        # Create the zip file
        with zipfile.ZipFile(temp, "w") as zip_file:
            # Walk the directory and add the files to the zip file
            for root, dirs, files in os.walk(directory):
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
