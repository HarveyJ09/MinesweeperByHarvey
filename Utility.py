import Settings

def height_prct(percentage):
    return int((Settings.HEIGHT / 100) * percentage)

print(height_prct(50)) # Example usage, prints 250 which is 50% of HEIGHT
def width_prct(percentage):
    return int((Settings.WIDTH / 100) * percentage)