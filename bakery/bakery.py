class cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if self.additives:
            print("Additives:")
            print("\t{}".format(self.additives))
        if self.filling:
            print("Filling : ")
            print(self.filling)
        print("*" * 20)


cake1 = cake('Vannila Cake', 'cake', 'vanilla', 'vanilla', 'cream')
cake2 = cake('chockolate cake', 'cake', 'chockolate', 'chockolate', 'nutella')
cake3 = cake('lemon cake', 'cake', 'lemon', 'lemon', '')


bakery_offer = []
bakery_offer.append(cake1)
bakery_offer.append(cake2)
bakery_offer.append(cake3)

print("Today in our offer:")
for c in bakery_offer:
    c.show_info()
