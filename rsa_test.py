from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_sign():
    datas = open('message.json').read()
    data = json.loads(datas, encoding="utf-8")
    data = json.dumps(data, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    print "signdata:~~~~~~~~", data
    key = RSA.importKey(open('private.pem').read())
    h = SHA256.new(data)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    return signature


def verify():
    signs = get_sign()
    pubkey = RSA.importKey(open('public.pem').read())
    datas = open('message.json').read()
    data = json.loads(datas, encoding="utf-8")
    data = json.dumps(data, ensure_ascii=False, separators=(',', ':'), sort_keys=True)

    print "verifydata:~~~~~~~", data
    digest = SHA256.new(data)
    pkcs = PKCS1_v1_5.new(pubkey)
    print pkcs.verify(digest, signs)
    return pkcs.verify(digest, signs)


verify()
