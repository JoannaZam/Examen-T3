from AlbumDigital import AlbumDigital
class Playlist(AlbumDigital):

    def __init__(self):
        super().__init__()
        self._nombre_playlist= ""
        self._usuario_creador = ""
        self._fecha_creacion = ""
        self._duracion_total =""
        self._lista_canciones = ""

    def get_nombre_playlist(self):
        return self._nombre_playlist

    def set_nombre_playlist(self, nombre_playlist):
        self._nombre_playlist = nombre_playlist

    def get_usuario_creador(self):
        return self._usuario_creador

    def set_usuario_creador(self, usuario_creador):
        self._usuario_creador = usuario_creador

    def get_fecha_creacion(self):
        return self._fecha_creacion

    def set_fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    def get_duracion_total(self):
        return self._duracion_total

    def set_duracion_total(self, duracion_total):
        self._duracion_total = duracion_total

    def get_lista_canciones(self):
        return self._lista_canciones

    def set_lista_canciones(self, lista_canciones):
        self._lista_canciones = lista_canciones

    def mostrarInformacionPlaylist(self):
        return f"Nombre: {self._nombre_playlist}, Creador: {self._usuario_creador}, Creación: {self._fecha_creacion}, Duracion: {self._duracion_total}, Playlist: {self._lista_canciones}"