# TODO: validate if command exists or launch defaults.
from os import path

from sharing import colors

# Super Key
mod = "mod4"
# Alt Key
alt = "mod1"

# Set Qtile config path
config_path = path.join(path.expanduser("~"), ".config", "qtile")
# Set Wallpapers path
wallpaper_path = path.join(path.expanduser("~"), "Pictures", "Wallpapers")

# Set Wallpaper
un_wallpaper = f"{wallpaper_path}/wallpaper_19.png"
# Set default font
un_font = "JetBrainsMono Nerd Font"
# Set color theme
un_theme = colors.Nord

# Set Default Terminal
un_terminal = "wezterm"
# Set Default Web Browser
un_browser = "firefox"
# Set Default Code Editor
un_ui_editor = "zeditor"
# Set Default Text Editor
un_cli_editor = "wezterm start nvim"
# Set Default ScreenShooter
un_screenshoot = "xfce4-screenshooter"
