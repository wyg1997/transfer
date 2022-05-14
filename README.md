# Transfer

Transfer files simply in shell.

## install

### clone and install

```shell
git clone https://github.com/wyg1997/transfer.git
cd transfer
pip install .
```

### from PyPI

TODO

## Usage

run `transfer -h` in shell.

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
