def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
		
def modinv2(a, m):
	try:
		return pow(a, -1, m)
	except:
		raise Exception('Modular inverse does not exist')
		
def moddiv(a, b, m):
	"""Calculates result (c) of a/b (mod m), c = a * b⁻¹ (mod m)"""
	a = a%m
	inv = modinv2(b,m)
	return a*inv%m
	