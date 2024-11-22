from Artista import Artista
class AlbumCasette(Artista):

    def __init__(self):
        super().__init__()
        self.titulo_casette= ""
        self.ventas = ""
        self.temas_comunes = ""
        self.compatibilidad = ""
        self.velocidad = ""

    def get_titulo_casette(self):
        return self.titulo_casette

    def set_tuitulo_casette(self, titulo_casette):
        self.titulo_casette = titulo_casette

    def get_ventas(self):
        return self.ventas

    def set_ventas(self, ventas):
        self.ventas = ventas

    def get_temas_comunes(self):
        return self.temas_comunes

    def set_temas_comunes(self, temas_comunes):
        self.temas_comunes = temas_comunes

    def get_compatibilidad(self):
        return self.compatibilidad

    def set_compatibilidad(self, compatibilidad):
        self.compatibilidad = compatibilidad

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def mostrarInformacionAlbumCasette (self):
        return f"Titulo de Almbum Casette:  {self.titulo_casette}, Ventas: {self.ventas}, Temas comunes: {self.temas_comunes}, Compatibilidad: {self.compatibilidad}, Velocidad: {self.velocidad}"
