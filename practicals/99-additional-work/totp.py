# totp code generator using documentation found at https://www.rfc-editor.org/rfc/rfc6238.html
# !!! does generate the same number as other totp generators

import time
import hashlib
import hmac


def generate_totp(shared_secret, token_time=30, length=6):
    now = time.time()
    step = int(now // token_time)
    hash = hmac.new(  # FIXME: more research required to ensure I am generating the hash correctly
        bytes(shared_secret, 'utf-8'),
        msg=bytes(step),
        digestmod=hashlib.sha256
    ).hexdigest()
    return dynamic_truncation(hash, length)


# FIXME: I believe there are issues in the dynamic truncation function, some more research is required.
def dynamic_truncation(string, length):
    stringbits = bin(int(string, base=16))  # use base 16 as string is in hex and has to be int for bin function
    offset = int(stringbits[-4:], base=2) * 8  # low-order bits are to the right  # * 8 is used to convert back to bytes
    selection = str(int(stringbits[offset:offset + 31], 2))
    return selection[-length:]

