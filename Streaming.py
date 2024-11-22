from AlbumDigital import AlbumDigital
class Streaming(AlbumDigital):

    def __init__(self):
        super().__init__()
        self._plataforma = ""
        self._formato = ""
        self._fecha_agregado = ""
        self._pais_disponible = ""

    def get_plataforma(self):
        return self._plataforma

    def set_plataforma(self, plataforma):
        self._plataforma = plataforma

    def get_formato(self):
        return self._formato

    def set_formato(self, formato):
        self._formato = formato

    def get_fecha_agregado(self):
        return self._fecha_agregado

    def set_fecha_agregado(self, fecha_agregado):
        self._fecha_agregado = fecha_agregado

    def get_pais_disponible(self):
        return self._pais_disponible

    def set_pais_disponible(self, pais_disponible):
        self._pais_disponible = pais_disponible

    def mostrarInformacionStreaming(self):
        return f"Plataforma: {self._plataforma}, Formato: {self._formato}, Se agrego el: {self._fecha_agregado}, Pais disponible: {self._pais_disponible}"


