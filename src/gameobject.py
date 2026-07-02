class GameObject:

    def __init__(self, name = "", x = 0, y =0 , color = (0,0,0), w = 0, h = 0, childs = []):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.childs = childs

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

    def get_name(self):
        return self.name
