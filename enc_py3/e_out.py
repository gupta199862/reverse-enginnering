# Time Succses Parser : Mon Jun 29 00:08:43 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import marshal, zlib, base64
kun = input('# file: ')
fileopen = open(kun, 'rb').read()
a = compile(fileopen, 'dg', 'exec')
m = marshal.dumps(a)
z = zlib.compress(m)
b = base64.b16encode(z)
c = kun.replace('.py', 'e.py')
d = open(c, 'w').write('# Encrypt by Sumarr ID\n# RECODE_BERKELAS\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode(' + str(b) + '))))')
print('# hasil: ' + c)