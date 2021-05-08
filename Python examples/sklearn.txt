from sklearn import datasets
iris = datasets.load_linnerud()
digits=datasets.load_digits()
print(digits)
print(digits.data)
print(digits.target)
print(digits.images[0])