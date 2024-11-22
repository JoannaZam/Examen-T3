from Genero import Genero
from Artista import Artista
from AlbumAcetato import AlbumAcetato
from AlbumCasette import AlbumCasette
from AlbumDigital import AlbumDigital
from Streaming import Streaming
from Playlist import Playlist

def main():

    print("Género")
    genero = Genero()
    genero.set_nombre_genero("Pop\n")
    genero.set_caracteristicas("Melodías pegajosas, letras accesibles, y temas como el amor y el desamor.\n")
    genero.set_origen("Estados Unidos y Reino Unido, influenciado por rock y jazz.\n")
    genero.set_fecha_inicio("1950s\n")
    genero.set_popularidad("Es el género más popular y comercial desde los años 60.\n")
    print(genero.mostrarInformacionGenero())

    print("\nArtista")
    artista = Artista()
    artista.set_nombre("Norma Monserrat Bustamante Laferte\n")
    artista.set_pais_origen("Chile\n")
    artista.set_fecha_inicio("2003\n")
    artista.set_premios("Grammy Latino, MTV Europe Music Award, Premios Pulsar\n")
    print(artista.mostrarInformacionArtista())

    print("\nÁlbum Acetato")
    album1 = AlbumAcetato()
    album1.set_tuitulo_acetato("Norma\n")
    album1.set_fecha_lanzamiento("9 de noviembre de 2018\n")
    album1.set_numero_canciones("10\n")
    album1.set_canciones_AlbumAcetato("\n◦Pa' Dónde Se Fue\n◦Si Tú Me Quisieras\n◦Por Qué Me Fui a Enamorar de Ti\n")
    album1.set_sello_discografico("Universal Music México\n")
    print(album1.mostrarInformacionAlbumAcetato())

    print("\nÁlbum Casette")
    album2 = AlbumCasette()
    album2.set_tuitulo_casette("Mon Laferte Vol. 1\n")
    album2.set_ventas("Edición limitada en formato casette, altamente coleccionable\n")
    album2.set_temas_comunes("Desamor, Nostalgia, Crecimiento personal\n")
    album2.set_compatibilidad("Con cualquier reproductor de casetes estándar\n")
    album2.set_velocidad("1⅞ pulgadas por segundo (4,76 cm/s)")
    print(album2.mostrarInformacionAlbumCasette())

    print("\nÁlbum Digital")
    album3 = AlbumDigital()
    album3.set_tuitulo_digital("SEIS\n")
    album3.set_colaboraciones("Alejandro Fernández, Ed Maverick, Natalia Lafourcade\n")
    album3.set_premios("Premio Billboard de la Música Latina 2022 (nominada)\n")
    album3.set_descargable("Disponible para descarga en plataformas como Spotify, Apple Music, y Google Play\n")
    print(album3.mostrarInformacionAlmbumDigital())

    print("\nStreaming")
    streaming = Streaming()
    streaming.set_plataforma("Spotify\n")
    streaming.set_formato("MP3. Álbum completo\n")
    streaming.set_fecha_agregado("10 de febrero de 2022\n")
    streaming.set_pais_disponible("Disponible globalmente\n")
    print(streaming.mostrarInformacionStreaming())

    print("\nPlaylist")
    playlist = Playlist()
    playlist.set_nombre_playlist("SEIS (2022) - Mon Laferte\n")
    playlist.set_usuario_creador("Mon Laferte\n")
    playlist.set_fecha_creacion("10 de febrero de 2022\n")
    playlist.set_duracion_total("42 minutos\n\n")
    playlist.set_lista_canciones("\n◦Antes de Ti\n◦Seis\n◦Lo Siento\n◦Casi Te Envidio\n◦Mi Buen Amor\n◦Perdón\n◦Mujer\n◦Quiero Ser\n◦Niña Bien\n◦La Sombra\n")
    print(playlist.mostrarInformacionPlaylist())

if __name__ == "__main__":
    main()
