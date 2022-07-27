import argparse

from transfer.core import upload, download, paste
from transfer.version import __version__


def parse_args():
    arg_parser = argparse.ArgumentParser(
        prog="transfer", description="Transfer files simply in shell."
    )
    arg_parser.add_argument("-V", "--version", action="version", version=__version__)
    arg_parser.set_defaults(func=lambda _: arg_parser.print_help())
    sub_parser = arg_parser.add_subparsers(help="sub-command")

    # upload
    upload_parser = sub_parser.add_parser("upload", help="upload file(s)")
    upload_parser.set_defaults(func=upload)
    upload_parser.add_argument(
        "-e", "--encrypt", action="store_true", help="encrypt file(s)"
    )
    upload_parser.add_argument("target", help="target directory or file to upload")

    # download
    download_parser = sub_parser.add_parser("download", help="download file")
    download_parser.set_defaults(func=download)
    download_parser.add_argument(
        "-d", "--decrypt", action="store_true", help="decrypt file"
    )
    download_parser.add_argument("-o", "--output", help="output file path or name")
    download_parser.add_argument("url", help="url to download")

    # paste
    paste_parser = sub_parser.add_parser("paste", help="paste text to web")
    paste_parser.set_defaults(func=paste)
    paste_parser.add_argument(
        "--expires",
        choices=["once", "1h", "1d", "1w", "21d"],
        help="expire time",
        default="21d",
    )
    paste_parser.add_argument(
        "--type", help="The type of target file. It decides which lexer to use."
    )
    paste_parser.add_argument("target", help="target file to paste text")

    return arg_parser.parse_args()
