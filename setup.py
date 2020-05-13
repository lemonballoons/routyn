from setuptools import setup

APP = ['routyn.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'mission-control.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}
#icon from Good Stuff No Nonsense
setup(
    app=APP,
    name='routyn',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps'])
