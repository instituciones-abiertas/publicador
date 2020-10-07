from __future__ import print_function

import os
from  ..abstract import Strategy
from cd_drive import Drive
import mimetypes

class GoogleDrive(Strategy):

    def __init__(self, credentials_file, path) -> None:
        self.credentials_file = credentials_file
        self.path = path

    def publicacion(self, archivo: str) -> str:
        mimetypes.init()
        mimetype = mimetypes.guess_type(archivo)[0] or 'text/plain'
        filename = os.path.basename(archivo)

        drive = Drive(self.credentials_file)
        drive.cd(self.path)
        drive.write(filename, mimetype, archivo)
