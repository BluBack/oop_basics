from praks5.konto import Konto

paul_konto = Konto("Paul", 100.00)
jakob_konto = Konto("Jakob", 500.00)

print("Algne saldo")
print(paul_konto.naita_saldo())
print(jakob_konto.naita_saldo())

jakob_konto.ylekanne(250.00)
print("Jakobi saldo nüüd on {0}".format(jakob_konto.naita_saldo()))
paul_konto.deposiit(250.00)
print("Pauli saldo nüüd on {0}".format(paul_konto.naita_saldo()))

print("Lõplik seisund")
print(paul_konto.naita_saldo())
print(jakob_konto.naita_saldo())