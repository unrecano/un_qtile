from typing import List

from libqtile.config import Click, Drag, Mouse
from libqtile.lazy import lazy

from sharing.constants import mod

def my_mouse() -> List[Mouse]:
    return [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]
