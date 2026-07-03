from pygame import Surface, draw
import src.variables as variables

def render_gameobjects(surface: Surface, objects = variables.GAMEOBJECTS):

    for object in objects:
        draw.rect(surface, object.color, (object.x, object.y, object.w, object.h))

        if object.get_childs() != []:
            render_gameobjects(surface, object.get_childs())
