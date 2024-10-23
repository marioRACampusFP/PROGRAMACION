playlist = []
while True:
    canciones = input("Escribe los nombres de las canciones que quieras y si no quieres más escribe 'fin': ")
    if canciones != "fin":
        playlist.append (canciones)
    else:
        break

print("Playlist")
for i, canciones in enumerate (playlist, start=1):
    print(f"{i +1}. {canciones}")
       

reproduccion = int(input("Escribe la canción que quieras volver a reproducir: ")) -1
print(f"Reproduciendo: {playlist[reproduccion]}")
    
