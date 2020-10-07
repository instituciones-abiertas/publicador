from __future__ import print_function

import os
from  ..abstract import Strategy
from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools
import mimetypes

class GoogleDrive(Strategy):
    def publicacion(self, archivo: str) -> str:
        res = self.upload(archivo)
        return res

    def upload(self, archivo: str):
        global file
        SCOPES = 'https://www.googleapis.com/auth/drive'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        store = file.Storage(os.path.join(dir_path, 'storage.json'))
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(os.path.join(dir_path,'client_id.json'), SCOPES)
            creds = tools.run_flow(flow, store)

        drive_service = discovery.build('drive', 'v3', http=creds.authorize(Http()))

        mimetypes.init()
        file_mimetype = mimetypes.guess_type(archivo)[0] or 'text/plain'
        file_metadata = {'name': os.path.basename(archivo) }
        media = MediaFileUpload(archivo, mimetype=file_mimetype)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
