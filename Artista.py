from Genero import Genero
class Artista(Genero):

    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._pais_origen = ""
        self._fecha_inicio = ""
        self._premios = ""

    # Getter y Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_pais_origen(self):
        return self._pais_origen

    def set_pais_origen(self, pais_origen):
        self._pais_origen = pais_origen

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def get_premios(self):
        return self._premios

    def set_premios(self, premios):
        self._premios = premios

    def mostrarInformacionArtista(self):
        return f"Nombre: {self._nombre}, Pais de origen: {self._pais_origen}, Fecha de inicio: {self._fecha_inicio}, Premios: {self._premios}"
