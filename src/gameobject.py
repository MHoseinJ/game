class GameObject:

    def __init__(self):
        self.name = ""
        self.x = 0
        self.y = 0
        self.color = (0,0,0)
        self.w = 0
        self.h = 0

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_size(self, w, h):
        self.w = w
        self.h = h

    def set_color(self, color):
        self.color = color

    def set_name(self, name):
        self.name = name

    def draw(self):
        return 0
