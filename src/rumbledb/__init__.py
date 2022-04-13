from .rumbledb import RumbleDBMagic

def load_ipython_extension(ipython):
    ipython.register_magics(RumbleDBMagic)
