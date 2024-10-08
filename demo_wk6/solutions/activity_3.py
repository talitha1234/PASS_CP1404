stream_to_shows = {"Netflix": ["Glitch", "Kath and Kim", "The Mole"],
                   "Prime": ["Invicible", "The Boys", "Fallout", "The Man in the High Castle"]}

# Task 1 - List all the streaming services
# Solution 1a - for loop
print("Streaming services I'm subscribed to: ")
for stream in stream_to_shows:
    print(stream)

# Solution 1b - slight difference
print("Streaming services I'm subscribed to: ")
for stream in stream_to_shows.keys():
    print(stream)

# Solution 1c - list generator
print("Streaming services I'm subscribed to: ")
print("\n".join(stream for stream in stream_to_shows.keys()))


# Task 2 - List all the Prime shows
# Solution 2a
print("My Favourite shows on Prime right now are: ")
for shows in stream_to_shows["Prime"]:
    print(shows)

# Solution 2b
print("My Favourite shows on Prime right now are: ")
"/n".join(show for show in stream_to_shows["Prime"])

# Task 3 - Print the show with the longest name - The Man in the High Castle
print("Longest show name: ")
longest_name = ''
for shows in stream_to_shows.values():
    for show in shows:
        if len(show) > len(longest_name):
            longest_name = show
print(longest_name)

# Task 4 - Add new show to one of the streaming services
# Solution 4a:
stream_to_shows["Netflix"] += ["Star Trek: The Next generation"]
print("New show added:")
print(stream_to_shows)

# Solution 4b
stream_to_shows["Netflix"].append("Star Trek: The Next generation")
print("New show added:")
print(stream_to_shows)

# Task 5 - Add new streaming service with one show
stream_to_shows["Binge"] = "Love & Death"
print(stream_to_shows)


# Task 6 - Remove one of the streaming services
del stream_to_shows["Binge"]
print(stream_to_shows)
