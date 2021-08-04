def mod_5(x):
    """return the reminder of x after dividing by 5"""
    return x % 5

print(
    'which number is biggest?',
    max(1000,511, 141),
    'which number is the biggest modulo 5?',
    max(1000, 511, 141, key=mod_5),
    sep='\n'
)