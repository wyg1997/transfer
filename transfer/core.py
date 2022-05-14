import os
import os.path as osp

from transfer.utils import compress_directory, check_gpg_install


# upload
_upload_command = "curl --upload-file {} https://transfer.sh/{}; echo ''"
_upload_with_encrypt_command = (
    'cat {} | gpg -ac -o- | curl -X PUT --upload-file "-" https://transfer.sh/{}'
    '; echo ""'
)


def upload(args):
    """
    Uploads file or directory to the server.
    """
    target = args.target
    assert osp.exists(target), f"{target} does not exist."

    if osp.isfile(target):
        basename = osp.basename(target)
        file = target
    else:
        basename = osp.dirname(target) + ".zip"
        file = compress_directory(target)

    if args.encrypt:
        check_gpg_install()
        command = _upload_with_encrypt_command.format(file, basename)
    else:
        command = _upload_command.format(file, basename)

    os.system(command)


# download
_download_command = "curl {} -o {}"
_download_and_decrypt_command = "curl {} | gpg -o- > {}"


def download(args):
    """
    Downloads file from the server.
    """
    url = args.url
    filename = url.split("/")[-1]
    if args.output is not None:
        path = args.output
        if osp.isdir(args.output):
            path = osp.join(path, filename)
    else:
        path = filename

    if args.decrypt:
        check_gpg_install()
        command = _download_and_decrypt_command.format(url, path)
    else:
        command = _download_command.format(url, path)

    os.system(command)


# paste
def paste(args):
    """
    Pastes text to the server.
    """
    raise NotImplementedError
