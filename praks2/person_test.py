from praks2.person import Person

kristo = Person()
kristo.setPerson('kristo', 16)
kristo.info()
kristo.age = kristo.age + 1
kristo.info()

margus = Person()
margus.setPerson('Margus', 45)
margus.info()