BASE62_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
BASE62_map = {key : idx for key, idx in enumerate(BASE62_CHARS)}


def base62_encode(num: int) -> str:
    if num == 0:
        return BASE62_CHARS[0]
    
    base62 = len(BASE62_CHARS)
    encoded = []

    while num > 0:
        num, rem = divmod(num, base62)
        encoded.append(BASE62_CHARS[rem])

    return ''.join(reversed(encoded))



