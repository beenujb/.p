str = 'a123'
try:
    n = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
