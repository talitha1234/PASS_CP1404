flowers = ['Roses', 'Violets', 'Hibiscus', 'Poppies', 'Frangipani', 'Daisy', 'Lily', 'Orchid']
colors = ['Red', 'Blue', 'Pink', 'Red', 'Yellow', 'Yellow', 'White', 'Purple']

flowers_to_colors = dict(zip(flowers, colors))

for flower, color in flowers_to_colors.items():
    print(f"The name of the flower is {flower} and they are typically {color} in color")
