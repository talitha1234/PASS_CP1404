stream_to_shows = {"Netflix": ["Glitch", "Kath and Kim", "The Mole"],
                   "Prime": ["Invincible", "The Boys", "Fallout", "The Man in the High Castle"]}

# Task 1 - List all the streaming services

print(f"Streaming services I'm subscribed to: ")
# code here
for stream in stream_to_shows.keys():
    if len(stream) < 5:
        print(stream)

print("".join(stream for stream in stream_to_shows.keys() if len(stream) > 5))
# NetflixPrime
# Netflix
# Prime

streams = (stream for stream in stream_to_shows.keys())
print(streams)
# <generator object <genexpr> at 0x000001AE28B08040>

streams = [stream for stream in stream_to_shows.keys()]
print(streams)
# ['Netflix', 'Prime']

for stream in streams:
    print(stream)

# Task 2 - List all the Prime shows
print("My Favourite shows on Prime right now are: ")
# code here
print(f"My Favourite shows on Prime right now are: ")

# Task 3 - Print the show with the longest name - The Man in the High Castle
print("Longest show name: ")
# code here

# Task 4 - Add new show to one of the streaming services

# Task 5 - Add new streaming service with one show
stream_to_shows['Disney Plus'] = 'Starwars'
print(stream_to_shows)
stream_to_shows['Binge'] = []
print(stream_to_shows)

# print(f" Jane's age is: {name_to_age['Jane']}")

# Task 6 - Remove one of the streaming services e.g. netflix

