"""
this code
ok?
"""


def print_musics(musics):
    for song in musics:
        print(song['name'], song['title'])
    print("the end")


if __name__ == "__main__":
    my_musics = [{'name': 'pist', 'title': 'lyly'},
                 {'name': 'or', 'title': 'tour'},
                 {'name': 'or1', 'title': 'tour3'},]
    print_musics(my_musics)

