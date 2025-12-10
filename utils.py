
def process_data(data: dict) -> dict:
    '''Process incoming data payload'''
    cleaned = {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}
    return cleaned


class ConfigManager:
    def __init__(self, path: str):
        self.path = path
        self._cache = {}

    def get(self, key):
        return self._cache.get(key)

