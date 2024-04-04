import heapq
from collections import defaultdict

def shuffleSong(tracks):
    library = defaultdict(list)
    for track in tracks:
        song, artist = track
        library[artist].append(song)


    heap = []
    for key in library:
        heapq.heappush(heap, (-len(library[key]), key))

    # Continuously pick the highest and add it to the playlist,
    # then pick the next highest without inserting the first.

    previous = None
    playlist = []

    while heap:
        cnt, artist = heapq.heappop(heap)
        cnt = -cnt
        playlist.append((library[artist][0], artist))
        library[artist].pop(0)
        cnt-=1

        # This is the main intuition
        if previous:
            if previous[0]!=0:
                heapq.heappush(heap, previous)

        previous = (-cnt, artist)

    return playlist if len(playlist) == len(tracks) else "Not Possible"


if __name__ == "__main__":
    tracks = [("songA", "artistA"), ("songB", "artistB"), ("songB", "artistB"), ("songC", "artistA"), ("songB", "artistB"),("songB", "artistB"),]
    print(shuffleSong(tracks))