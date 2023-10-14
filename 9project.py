import numpy as np

M = 4
N = 5

masiv = np.random.randint(1, 23, size=(M, N))

print("Початковий масив:")
print(masiv)

suma = masiv[0, 0] + masiv[0, -1] + masiv[-1, 0] + masiv[-1, -1]
print(f"Сума елементів по кутам масиву: {suma}")

average = np.mean(masiv)

masiv[masiv < average] = 0

print("Масив після заміни:")
print(masiv)
