import hashlib
from itertools import count

def mine_coin(key: str, digits: int = 5) -> int:
    for i in count():
        m = hashlib.md5()
        inc_key = key + str(i)
        m.update(inc_key.encode('utf-8'))
        h = m.hexdigest()
        if h[0:digits] == '0'*digits:
            return i

