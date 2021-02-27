"""An unofficial Python wrapper for the Binance exchange API v3

.. moduleauthor:: Sam McHardy

"""

__version__ = '0.7.3.1-dev'

from binance.client import Client, AsyncClient  # noqa
from binance.depthcache import DepthCacheManager  # noqa
from binance.websockets import BinanceSocketManager  # noqa
