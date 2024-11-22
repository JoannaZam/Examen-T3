from Artista import Artista
class AlbumDigital(Artista):

    def __init__(self):
        super().__init__()
        self.titulo_digital= ""
        self.colaboraciones = ""
        self.premios = ""
        self.descargable= ""

    def get_titulo_digital(self):
        return self.titulo_digital

    def set_tuitulo_digital(self, titulo_digital):
        self.titulo_digital = titulo_digital

    def get_colaboraciones(self):
        return self.colaboraciones

    def set_colaboraciones(self, colaboraciones):
        self.colaboraciones = colaboraciones

    def get_premios(self):
        return self.premios

    def set_premios(self, premios):
        self.premios = premios

    def get_descargable(self):
        return self.descargable

    def set_descargable(self, descargable):
        self.descargable = descargable


    def mostrarInformacionAlmbumDigital(self):
        return f"Titulo de Album Digital: {self.titulo_digital}, Colaboraciones: {self.colaboraciones}, Premios: {self.premios}, Descargable: {self.descargable}"