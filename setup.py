"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["src/textinator.py"]

# Include additional python modules here; probably not the best way to do this
# but I couldn't figure out how else to get py2app to include modules in the src/ folder
DATA_FILES = [
    "src/icon.png",
    "src/icon_paused.png",
    "src/loginitems.py",
    "src/macvision.py",
    "src/pasteboard.py",
    "src/utils.py",
]

OPTIONS = {
    "iconfile": "icon.icns",
    "plist": {
        "LSUIElement": True,
        "NSDesktopFolderUsageDescription": "Textinator needs access to your Desktop folder to detect new screenshots. "
        "If you have changed the default location for screenshots, "
        "you will also need to grant Textinator full disk access in "
        "System Preferences > Security & Privacy > Privacy > Full Disk Access.",
        "NSAppleEventsUsageDescription": "Textinator needs permission to send AppleScript events to add itself to Login Items.",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    name="Textinator",
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
