# Simple in-memory cache
import time
_cache = {}

def get(key):
    v = _cache.get(key)
    if not v: return None
    val, exp = v
    if time.time() > exp:
        del _cache[key]
        return None
    return val

def set(key, value, ttl=300):
    _cache[key] = (value, time.time()+ttl)
