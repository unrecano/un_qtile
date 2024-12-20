from typing import Any, List, Tuple

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from sharing.constants import mod


def _init_group_names() -> List[Tuple[str, Any]]:
    return [
        # Icon: nf-md-firefox
        ("web", {"label": "󰈹 WEB", "layout": "max"}),
        # Icon: nf-oct-file_code
        ("code", {"label": " CODE", "layout": "monadtall"}),
        # Icon: nf-oct-terminal
        ("term", {"label": " TERM", "layout": "monadtall"}),
        # Icon: nf-md-skull_scan
        ("misc", {"label": "󱓇 MISC", "layout": "max"}),
    ]


def my_groups() -> List[Group]:
    return [Group(name, **kwargs) for name, kwargs in _init_group_names()]


def _shortcuts_by_group(number: int, group: Group) -> List[Key]:
    return [
        # mod + group number = switch to group
        Key(
            [mod],
            str(number),
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        ),
        # mod + shift + group number = switch to & move focused window to group
        Key(
            [mod, "shift"],
            str(number),
            lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(
                group.name
            ),
        ),
        # Or, use below if you prefer not to switch to that group.
        # # mod + shift + group number = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ]


def groups_keymap(groups: List[Group]) -> List[Key]:
    return [
        key
        for i, group in enumerate(groups, start=1)
        for key in _shortcuts_by_group(i, group)
    ]
