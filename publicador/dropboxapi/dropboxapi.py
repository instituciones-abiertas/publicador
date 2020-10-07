from ..abstract import Strategy
import dropbox, os
from decouple import config

DROPBOX_TOKEN = config('DROPBOX_TOKEN', default='')

class DropboxApi(Strategy):
    def publicacion(self, archivo: str) -> str:
        dropbox_path= '/example'
        file_basename = os.path.basename(archivo)
        client = dropbox.Dropbox(DROPBOX_TOKEN, scope=['files.content.write'])
        client.files_upload(open(archivo, "rb").read(), os.path.join(dropbox_path, file_basename), mode=dropbox.files.WriteMode.overwrite)
        print("[UPLOADED] {}".format(archivo))
        return 'Ok'
