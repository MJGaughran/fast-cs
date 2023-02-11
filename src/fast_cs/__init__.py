from importlib.metadata import version

from pydantic import BaseSettings

from .controller import Controller

__version__ = version("fast-cs")
del version

__all__ = ["__version__", "Controller", "BaseSettings"]
