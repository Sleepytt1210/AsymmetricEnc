from math import gcd
from optparse import OptionParser
from utils import modinv2
import sys

p = 257
q = 263
e = 31

parser = OptionParser()
parser.add_option("-p", "--pprime", dest="p", action="store",
                  help="Prime number p", type="int")
parser.add_option("-q", "--qprime", action="store", dest="q",
                  help="Prime number q", type="int")
parser.add_option("-e", "--exponent", action="store", dest="e",
                  help="Public key/exponent e", type="int")
parser.add_option("-m", "--message", action="store", dest="m",
                  help="Message", type="int")
(options, args) = parser.parse_args()

if options.p:
	p = options.p
if options.q:
	q = options.q
if options.e:
	e = options.e
N = p * q
fN = (p-1) * (q-1)
m = 123 if not options.m else options.m

denom = gcd(e, fN)

if denom != 1:
	sys.stderr.write("gcd of e and Φ(N) is not equal to 1!\n")
	sys.exit(0)


print("gcd of e and fN:", denom)

print ("fN is:", fN)

d = modinv2(e, fN)
print("Multiplicative inverse of", e, "mod", fN, "is", d)

c = pow(m, e, N)
print ("Message =", m, ", Ciphered =", c)
print ("Deciphered =", pow(c, d, N))