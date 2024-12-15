from typing import List

from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

from sharing.constants import alt, mod, un_browser, un_cli_editor, un_screenshoot, un_terminal, un_ui_editor

def _default_key_bindings() -> List[Key]:
    return [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows.
        Key([mod], "i", lazy.layout.grow()),
        Key([mod], "m", lazy.layout.shrink()),
        Key([mod], "n", lazy.layout.reset()),
        Key([mod, "shift"], "n", lazy.layout.normalize()),
        Key([mod], "o", lazy.layout.maximize()),
        Key([mod, "shift"], "s", lazy.layout.toggle_auto_maximize()),
        Key([mod, "shift"], "space", lazy.layout.flip()),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key(
            [mod],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        Key([mod], "g", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    ]

def _key_bindings_to_switch_vts() -> List[Key]:
    return [
        Key(
            ["control", alt],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}"
        )
        for vt in range(1, 8)
    ]

def _custom_key_bindings() -> List[Key]:
    return [
        # Toggle between layouts.
        Key([mod], "tab", lazy.next_layout()),
        Key([mod, "shift"], "tab", lazy.prev_layout()),
        # Sound
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
        # Brightness
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
        Key([], "Print", lazy.spawn(un_screenshoot)),
        # Devices
        Key([mod, alt], "b", lazy.spawn("rfkill toggle bluetooth"), desc="Turn on/off Bluetooth Adapter"),
        # Applications.
        Key([mod], "t", lazy.spawn(un_terminal), desc="Launch favorite terminal"),
        Key([mod], "b", lazy.spawn(un_browser), desc="Launch favorite Web Browser"),
        Key([mod], "c", lazy.spawn(un_ui_editor), desc="Launch favorite Editor"),
        Key([mod, alt], "c", lazy.spawn(un_cli_editor), desc="Launch favorite Editor for Terminal"),
        Key([mod], "e", lazy.spawn("thunar"), desc="Launch File Manager"),
    ]

def my_keymap() -> List[Key]:
    return [
        *_default_key_bindings(),
        *_key_bindings_to_switch_vts(),
        *_custom_key_bindings()
    ]
