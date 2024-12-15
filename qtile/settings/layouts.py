from typing import Any, Dict, List

from libqtile import layout
from libqtile.config import Match
from libqtile.layout.base import _SimpleLayoutBase

from sharing.constants import un_font, un_theme

def _custom_layout_theme() -> Dict[str, Any]:
    return {
        "border_width": 0,
        "margin": 4,
        "border_focus": un_theme[1],
        "border_normal": un_theme[1],
        "font": un_font,
    }

def _custom_monad_tall() -> layout.MonadTall:
    return layout.MonadTall(**_custom_layout_theme())

def floating_layout() -> layout.Floating:
    return layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ],
        **_custom_layout_theme(),
    )

def my_layouts() -> List[_SimpleLayoutBase]:
    return [
        # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        _custom_monad_tall(),
    ]
