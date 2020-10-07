# Publicador

File publisher to several cloud platforms
[Pypi Package link](https://pypi.org/project/publicador/)

## Support

- Googledrive
- Dropbox

## Deps

In order to use you need to:
- [Enable google drive api in you account](https://developers.google.com/drive/api/v3/enable-drive-api)
- [Create an dropbox app and get token](https://www.dropbox.com/developers/)

## Install

`pip install publicador`

## Usage
> Publish input.docx on Googledrive and Dropbox

```
from publicador import Publicador
from publicador import GoogleDrive
from publicador import DropboxApi

credentials = 'path/to/credentials.json'
drivepath = '/example-dir'

context = Publicador('./input.docx', GoogleDrive(credentials, drivepath))
context.publicar()

# token = 'app_token_from_dropbox'
# dropxboxpath= '/example-dir'
# context.strategy = DropboxApi(token, dropboxpath)
# context.publicar()

```
