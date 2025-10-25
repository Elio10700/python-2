class USA:
    def capital(self):
        print("the capital of USA is Washington DC")

    def language(self):
        print("In USA,Widely spoken language is English")

    def type(self):
        print("USA is a developed country")

class India:
    def capital(self):
        print("the capital of India is New Delhi")

    def language(self):
        print("In India,Widely spoken language is Hindi")

    def type(self):
        print("India is a developing country")

obj1 = USA()
obj2 = USA()

for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()