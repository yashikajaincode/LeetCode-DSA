import random
import string

class Codec:
    def __init__(self):
        self.long2short = {}
        self.short2long = {}
        self.prefix = "http://tinyurl.com/"
        self.alphabet = string.ascii_letters + string.digits
        self.key_len = 6

    def _gen_key(self) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(self.key_len))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.long2short:
            return self.prefix + self.long2short[longUrl]
        key = self._gen_key()
        while key in self.short2long:
            key = self._gen_key()
        self.short2long[key] = longUrl
        self.long2short[longUrl] = key
        return self.prefix + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.rsplit('/', 1)[-1]
        return self.short2long.get(key, "")
