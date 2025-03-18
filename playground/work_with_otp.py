import datetime
import time

import jwt

secret = "kjhkjjjjhikhkjk"

payload = {
    "my_name": "Vasyl",
    "age": 45,
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=5),
}

encode_jwt = jwt.encode(payload=payload, key=secret, algorithm="HS256")
print(encode_jwt)
time.sleep(12)

decoded = jwt.decode(
    encode_jwt,
    secret,
    algorithms=["HS256"],
    # options={
    #     'verify_signature': False
    # }
)
print(decoded)
