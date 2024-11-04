from pico2d import load_image


class Grass:
    def __init__(self, y = 50):
        self.image = load_image('grass.png')
        self.x, self.y = 400, y

    def draw(self):
        self.image.draw(400, self.y)


    def update(self):
        pass
