"""ashlibによるハッシュ化の基本
pdkbf2_hmacの動作を自分で書いてみるとすると以下のようになる
"""
import base64
import hashlib
import os

# saltの生成
salt = base64.b64encode(os.urandom(32))
# hash化の回数
iter_num = 100000

password = "password01"
# ソルト(salt)を付け加えてからハッシュ化
digest = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
# ストレッチング(stretching)
for _ in range(iter_num):
    digest = hashlib.sha256(digest.encode("utf-8")).hexdigest()

print(digest)
