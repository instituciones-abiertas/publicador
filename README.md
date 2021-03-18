# IA² | publicador

<p align="center">
  <a target="_blank" rel="noopener noreferrer">
    <img width="220px" src="https://www.ia2.coop/public/ia2-logo-blue.png" alt="IA²" />
  </a>
</p>

<h4 align="center">File publisher for IA²</h4>

---

<p align="center" style="margin-top: 14px;">
  <a href="https://badge.fury.io/py/publicador">
    <img src="https://badge.fury.io/py/publicador.svg" alt="PyPI version" height="20">
  </a>
  <a href="https://pypi.org/project/publicador/">
    <img src="https://img.shields.io/pypi/dm/publicador.svg" alt="PyPI version" height="20">
  </a>
  <a
    href="https://github.com/instituciones-abiertas/publicador/blob/main/LICENSE"
  >
    <img
      src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"
      alt="License" height="20"
    >
  </a>
  <a
    href="https://github.com/instituciones-abiertas/publicador/blob/main/CODE_OF_CONDUCT.md"
  >
    <img
      src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"
      alt="Contributor Covenant" height="20"
    >
  </a>
</p>

## About

The `publicador` package helps with the uploading files process. It currently supports the following platforms:

- Googledrive
- Dropbox

## Pre-requisites

In order to use you need to setup a few credentials for the platform you need:

- [Enable google drive api in you account](https://developers.google.com/drive/api/v3/enable-drive-api)
- [Create an dropbox app and get token](https://www.dropbox.com/developers/)

## Install package via pip

```bash
pip install publicador
```

## Usage

> This example publishes an `input.docx` file to Googledrive and Dropbox

```python
from publicador import Publicador
from publicador import GoogleDrive
from publicador import DropboxApi

google_credentials = 'path/to/credentials.json'
drivepath = '/example-dir'

context = Publicador('./input.docx', GoogleDrive(google_credentials, drivepath))
context.publicar()

token = 'app_token_from_dropbox'
dropxbox_path= '/example-dir'
context.strategy = DropboxApi(token, dropxbox_path)
context.publicar()
```

## License

[**GNU General Public License version 3**](https://opensource.org/licenses/GPL-3.0)
