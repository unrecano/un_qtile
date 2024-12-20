from typing import Any, List

from libqtile import bar
from libqtile.config import Screen

from sharing.constants import un_theme, un_wallpaper


def built_in_screen(widgets: List[Any]) -> Screen:
    return Screen(
        top=bar.Bar(
            widgets=widgets,
            size=26,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            opacity=0.2,
            background=un_theme[0],
            margin=4,
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
        wallpaper=un_wallpaper,
        wallpaper_mode="stretch",
    )


def my_screens(widgets: List[Any]) -> List[Screen]:
    return [built_in_screen(widgets)]
