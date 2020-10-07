from ..abstract import Strategy
import dropbox, os

class DropboxApi(Strategy):

    def __init__(self, token, path) -> None:
        self.token = token
        self.path = path

    def publicacion(self, archivo: str) -> str:
        file_basename = os.path.basename(archivo)
        client = dropbox.Dropbox(self.token, scope=['files.content.write'])
        client.files_upload(open(archivo, "rb").read(), os.path.join(self.path, file_basename), mode=dropbox.files.WriteMode.overwrite)
        return "[UPLOADED] {}".format(archivo)
