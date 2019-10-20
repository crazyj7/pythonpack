'''
pip install jakecipher
'''
import jakecipher as jc

print('version=', jc.version)

# invfactor()
# Inverse Key Test
multikey=5
invkey = jc.inversefactor(multikey)
print(multikey, " multiply mod 26 inverse key=", invkey)

for pt in range(10):
    ct=pt*multikey % 26
    dt = ct*invkey % 26
    print(pt, ' enc=', ct, 'dec=', dt, '  ',
          'OK' if pt==dt else "FAIL")


plaintext = 'Hello World!!'
print("PLAINTEXT : ", plaintext)

# jake_encrypt() and jake_decrypt()

# manual key
# keys=[5,3, 3,1, 9,7, 5,5, 4]

# key generator :
keys = jc.make_jake_key("myPassword!")
print("KEYS : ", keys)

lastcipher=jc.jake_encrypt(keys, plaintext)
print("ENCRYPT")
print('---', lastcipher, '---  length=', len(lastcipher), sep='')

lastdec=jc.jake_decrypt(keys, lastcipher, False)
print("DECRYPT")
print('---',lastdec, '---  length=', len(lastdec), sep='')
lastdec=jc.jake_decrypt(keys, lastcipher)
print('---',lastdec, '---  length=', len(lastdec), sep='')

if plaintext.rstrip()==lastdec.rstrip():
    print("OK")
else:
    print("FAIL")


# debug list format print
jc.printlist("plain:  ", plaintext, 4, False)
jc.printlist("cipher: ", lastcipher, 4, False)
jc.printlist("decrypt:", lastdec, 4, False)

