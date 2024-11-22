from Artista import Artista
class AlbumAcetato(Artista):

    def __init__(self):
        super().__init__()
        self.titulo_acetato= ""
        self.fecha_lanzamiento = ""
        self.numero_canciones = ""
        self.canciones_AlbumAcetato = ""
        self.sello_discografico = ""

    def get_titulo_acetato(self):
        return self.titulo_acetato

    def set_tuitulo_acetato(self, titulo_acetato):
        self.titulo_acetato = titulo_acetato

    def get_fecha_lanzamiento(self):
        return self.fecha_lanzamiento

    def set_fecha_lanzamiento(self, fecha_lanzamiento):
        self.fecha_lanzamiento = fecha_lanzamiento

    def get_numero_canciones(self):
        return self.numero_canciones

    def set_numero_canciones(self, numero_canciones):
        self.numero_canciones = numero_canciones

    def get_canciones_AlbumAcetato(self):
        return self.canciones_AlbumAcetato

    def set_canciones_AlbumAcetato(self, canciones_AlbumAcetato):
        self.canciones_AlbumAcetato = canciones_AlbumAcetato

    def get_sello_discografico(self):
        return self.sello_discografico

    def set_sello_discografico(self, sello_discografico):
        self.sello_discografico = sello_discografico

    def mostrarInformacionAlbumAcetato(self):
        return f"Titulo de album: {self.titulo_acetato}, Lanzamiento: {self.fecha_lanzamiento}, Numero de canciones: {self.numero_canciones}, Sello discografico: {self.sello_discografico}, Algunas canciones: {self.canciones_AlbumAcetato}"