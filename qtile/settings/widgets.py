from typing import Any, Dict, List

from libqtile import widget

from sharing.constants import un_font, un_theme


def custom_widget_theme(
    background: List[str] = un_theme[0],
    foreground: List[str] = un_theme[1],
) -> Dict[str, Any]:
    return {
        "background": background,
        "foreground": foreground,
        "font": f"{un_font} Bold",
        "font_size": 13,
        "padding": 7,
    }


def custom_separator(padding: int = 10) -> Any:
    return widget.Sep(  # type: ignore
        background=un_theme[0],
        foreground=un_theme[1],
        linewidth=0,
        padding=padding,
    )


def custom_groupbox() -> Any:
    return widget.GroupBox(  # type: ignore
        font=un_font,
        font_size=24,
        borderwidth=3,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        active=un_theme[6],  # Active workspace
        inactive=un_theme[1],  # Inactive workspace
        rounded=False,
        highlight_method="block",
        block_highlight_text_color=un_theme[2],  # Current text workspace
        urgent_alert_method="block",
        urgent_border=un_theme[3],
        this_current_screen_border=un_theme[1],  # Current workspace
        disable_drag=True,
    )


def custom_window_name() -> List[Any]:
    return [
        # Icon: nf-md-application
        widget.TextBox(  # type: ignore
            **custom_widget_theme(), text="󰣆"
        ),
        widget.WindowName(  # type: ignore
            **custom_widget_theme(), empty_group_string="Desktop", max_chars=130
        ),
    ]


def custom_prompt() -> List[Any]:
    return [
        # Icon: nf-seti-search
        widget.TextBox(  # type: ignore
            **custom_widget_theme(),
            text="",
        ),
        widget.Prompt(  # type: ignore
            **custom_widget_theme(), cursor_color=un_theme[1][0], prompt=""
        ),
    ]


def custom_bluetooth() -> Any:
    # Icon: nf-fa-bluetooth
    return widget.Bluetooth(  # type: ignore
        **custom_widget_theme(foreground=un_theme[7]),
        default_text=" BT {connected_devices}",
        adapter_format="{name} [{powered}]",
    )


def custom_wlan() -> List[Any]:
    foreground = un_theme[8]
    return [
        # Icon: nf-fa-wifi
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text=""
        ),
        widget.Wlan(  # type: ignore
            **custom_widget_theme(foreground=foreground),
            format="{essid} {percent:2.0%}",
            ethernet_interface="lo",
            interface="wlp0s20f3",
        ),
    ]


def custom_net() -> List[Any]:
    foreground = un_theme[3]
    return [
        # Icon: nf-fa-network_wired
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text=""
        ),
        widget.Net(  # type: ignore
            **custom_widget_theme(foreground=foreground), interface="wlp0s20f3"
        ),
    ]


def custom_battery() -> List[Any]:
    foreground = un_theme[3]
    return [
        # Icon: nf-md-battery
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text="󰁹"
        ),
        widget.Battery(  # type: ignore
            **custom_widget_theme(foreground=foreground),
            low_foreground=foreground,
            charge_char="",
            discharge_char="",
            format="{percent:2.0%} {char} | {hour:d}:{min:02d}",
        ),
    ]


def custom_volume() -> List[Any]:
    foreground = un_theme[6]
    return [
        # Icon: nf-fa-volume_high
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text=""
        ),
        widget.Volume(**custom_widget_theme(foreground=foreground)),  # type: ignore
    ]


def custom_backlight() -> List[Any]:
    foreground = un_theme[5]
    return [
        # Icon: nf-md-brightness_7
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text="󰃠"
        ),
        widget.Backlight(  # type: ignore
            **custom_widget_theme(foreground=foreground),
            backlight_name="intel_backlight",
        ),
    ]


def custom_clock() -> List[Any]:
    foreground = un_theme[1]
    return [
        # Icon: nf-md-clock
        widget.TextBox(  # type: ignore
            **custom_widget_theme(foreground=foreground), text="󰥔"
        ),
        widget.Clock(  # type: ignore
            **custom_widget_theme(foreground=foreground), format="%a %I:%M %p"
        ),
    ]


def custom_check_updates() -> Any:
    # Icon: nf-md-download_box
    return widget.CheckUpdates(  # type: ignore
        **custom_widget_theme(),
        colour_have_updates=un_theme[4],
        colour_no_updates=un_theme[4],
        no_update_string="󱑢 0",
        display_format="󱑢 {updates}",
        update_interval=1800,
        custom_command="checkupdates",
    )


def custom_quick_exit() -> Any:
    # Icon: nf-iec-power
    return widget.QuickExit(  # type: ignore
        **custom_widget_theme(foreground=un_theme[2]),
        default_text="⏻",
        countdown_format="{}",
    )


def my_widgets() -> List[Any]:
    return [
        custom_separator(),
        custom_groupbox(),
        custom_separator(),
        *custom_prompt(),
        custom_separator(),
        *custom_window_name(),
        custom_bluetooth(),
        *custom_wlan(),
        # *custom_net(),
        *custom_battery(),
        *custom_volume(),
        *custom_backlight(),
        *custom_clock(),
        custom_check_updates(),
        widget.Systray(**custom_widget_theme()),  # type: ignore
        custom_quick_exit(),
        custom_separator(),
    ]
