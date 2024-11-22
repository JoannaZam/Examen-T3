class Genero:

    def __init__(self):
        self._nombre_genero= ""
        self._caracteristicas = ""
        self._origen = ""
        self._fecha_inicio = ""
        self._popularidad = ""

    # Getters y Setters
    def get_nombre_genero(self):
        return self._nombre_genero

    def set_nombre_genero(self, nombre_genero):
        self._nombre_genero = nombre_genero

    def get_caracteristicas(self):
        return self._caracteristicas

    def set_caracteristicas(self, caracteristicas):
        self._caracteristicas = caracteristicas

    def get_origen(self):
        return self._origen

    def set_origen(self, origen):
        self._origen = origen

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def get_popularidad(self):
        return self._popularidad

    def set_popularidad(self, popularidad):
        self._popularidad = popularidad

    def mostrarInformacionGenero(self):
        return f"Nombre del genero: {self._nombre_genero}, Caracteristicas: {self._caracteristicas}, Origen: {self._origen}, Fecha de inicio: {self._fecha_inicio}, Popularidad: {self._popularidad}"
