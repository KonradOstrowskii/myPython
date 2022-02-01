class cake:

    bakery_offer = []
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

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

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake1 = cake('Vannila Cake', 'cake', 'vanilla', 'vanilla', 'cream')
cake2 = cake('chockolate cake', 'cake', 'chockolate', 'chockolate', 'nutella')
cake3 = cake('lemon cake', 'cake', 'lemon', 'lemon', '')
cake4 = cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake5 = cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')


bakery_offer = []
bakery_offer.append(cake1)
bakery_offer.append(cake2)
bakery_offer.append(cake3)

print("Today in our offer:")
for c in cake.bakery_offer:
    c.show_info()
