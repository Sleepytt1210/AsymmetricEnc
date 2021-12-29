from math import gcd
from optparse import OptionParser

p = 257
q = 263
N = 67591
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

p = options.p
q = options.q
e = options.e
N = p * q
m = 123 if not options.m else options.m


denom = gcd(e, fN)

if denom != 1:
	sys.stderr.write("gcd of e and Φ(N) is not equal to 1!\n")
	sys.exit(0)
	
print("gcd of e and p-1: ", denom)

print ("p-1 is:\t",p-1)

d = 0

for i in range(1,p):
	if (gcd(p-1,i)==1 and i*e%(p-1)==1): 
		print("Multiplicative inverse of", e, "mod", p-1, "is", i)
		d = i
		break

c = pow(m, e, N)
print ("Message =", m, ", Ciphered ="
