v = [0xa8c567df,0x57af7154,0xf46c169b,0x403eec2f,0x374fb5c2,0xc61a4238,0x5a502b1a,0x590aa048,0x39ad2bc0,0x25ae89c9,0xe1dc2db2,0x9049374f,0xbc3344d7,0x89bbf1dc,0x143af3de,0xfcbd8dcb,0x1a8b3bbd,0xfe3d3c98,0xa2dd010f,0xcdc803a6,0x204d3099,0x289ad759,0xd26a9ad7,0x6f03feef,0xa6a53639,0xe8d669d3,0xbb2eae34,0xa375268e,0xf74e4875,0x417c175d,]
s = [0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,]

o = 0

k = []
for m, n in zip(v, s):
  if n:
    o ^= m
    k.append(m % 10000)

k.sort()
for mm in k:
  print "%.4i" % mm

print o