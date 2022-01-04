from math import gcd
from utils import modinv
from optparse import OptionParser

p = p
e = 23

parser = OptionParser()
parser.add_option("-p", "--pprime", dest="p", action="store",
                  help="Prime number p", type="int")
parser.add_option("-e", "--exponent", action="store", dest="e",
                  help="Public key/exponent e", type="int")
parser.add_option("-m", "--message", action="store", dest="m",
                  help="Message", type="int")
(options, args) = parser.parse_args()

if options.p:
	p = options.p
if options.e:
	e = options.e
m = 123 if not options.m else options.m


print ("p-1 is:\t",p-1)
denom = gcd(e, p-1)

if denom != 1:
	sys.stderr.write("gcd of e and p-1 is not equal to 1!\n")
	sys.exit(0)

d = modinv(e, p-1)
print("Mult inverse=", d)

c = pow(m, e, p)
print("Message =", m, ", Ciphered =", c)
print("Deciphered =", pow(c, d, p))