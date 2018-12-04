def make_album (artist_name, album_title, no_tracks = ''):
    if no_tracks:
        musicdict = {'artist': artist_name, 'album': album_title, 'tracks': no_tracks}
    else:
        musicdict = {'artist': artist_name, 'album': album_title}
    return musicdict

x = make_album ("pink floyd", "dark side of the moon", 10)
y = make_album ("led zeppelin", "IV")
z = make_album ("laurence", "yoyogi park")

print(x)
print(y)
print(z)

while True:
    print()
    print ("(Enter 'q' to quit)")
    a_in = input("Enter artist name :")
    if a_in=='q':
        break
    b_in = input("Enter album title :")
    if b_in=='q':
        break

    userdict = make_album(a_in, b_in)
    print(userdict)