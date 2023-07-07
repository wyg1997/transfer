# Transfer

Transfer files simply in shell.

upload and download powered by [https://transfer.sh/](https://transfer.sh/).

## Install

### 1. from PyPI (Recommended)

```shell
pip install file-transfer-tools
```

### 2. clone and install

```shell
git clone https://github.com/wyg1997/transfer.git
cd transfer
pip install .
```

## Usage

Run `transfer -h` in shell to see usage.

### upload

```shell
transfer upload <directory/file>
```

### upload with password

> NOTE: You should install GnuPG firstly.

```shell
transfer upload -e <directory/file>
" or transfer upload --encrypt <directory/file>
" and type password
```

### download

```shell
transfer download [-o <target_path>] <url>
```

### download encrypted file

```shell
transfer download -d [-o <target_path>] <url>
```

### paste

Paste the content of file to [https://pastebin.mozilla.org/](https://pastebin.mozilla.org/).

```shell
transfer paste [-h] [--expires {once,1h,1d,1w,21d}] [--type TYPE] target
```

> NOTE: All supported TYPE see [file type mapping.md](FILE_TYPE_MAPPING.md). But **you
needn't assign the type in most situation**, it will automatically choose a suitable type
according file extension.
