# Publicador

File publisher to several cloud platforms
[Pypi Package link](https://pypi.org/project/publicador/)

## Support

- Googledrive
- Dropbox

## Install

`pip install publicador`

## Usage
> Publish input.docx on Googledrive and Dropbox

```
from publicador import Publicador
from publicador import GoogleDrive
from publicador import DropboxApi

context = Publicador('./input.docx', GoogleDrive())
context.publicar()

context.strategy = DropboxApi()
context.publicar()

```
