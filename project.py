import random
import array as arr

masiv = arr.array('i', [random.randint(35, 55) 
for _ in range(12)])

print("Маси учнів підгрупи:")
print(masiv)

set1 = max(masiv)
counter = masiv.index(set1)

print(f"Найбільша маса: {set1}")
print(f"Номер учня, маса якого найбільша: {counter + 1}")
