import time

import numpy as np
import pxng
from pxng.colors import *

from ray import Color


def raytrace(window: pxng.Window):
    now = time.time()
    sprite: pxng.Sprite = window.context['sprite']

    w = sprite.width
    h = sprite.height
    for y in range(h):
        for x in range(w):
            c = Color(x / (w - 1), y / (h - 1))
            sprite.set_pixel(x, y, c.rgb())

    window.context['completed'] = True
    window.context['rendering_time'] = time.time() - now


def update(window: pxng.Window):
    if not window.context['completed']:
        raytrace(window)

    sprite: pxng.Sprite = window.context['sprite']
    window.draw_sprite(0, 0, sprite, scale=1)

    rendering_time = window.context["rendering_time"]
    window.draw_text(5, 5, f'Rendering Time: {rendering_time :.04f} s.', scale=0.5)


if __name__ == '__main__':
    w = 256
    h = 256
    sprite = pxng.Sprite(np.zeros((h, w, 3), dtype=np.uint8))
    window = pxng.Window(w * 2, h * 2, 'Raytracer', scale=2, vsync=True)

    window.context = {
        'sprite': sprite,
        'completed': False,
        'rendering_time': 0.0,
    }

    window.set_update_handler(update)
    window.start_event_loop()
