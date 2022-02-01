class cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)


class NoDuplicates:

    def __init__(self, funct):
        self.funct = funct

    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            if a not in cake.additives:
                no_duplicate_list.append(a)
        self.funct(cake, no_duplicate_list)


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake1 = cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake2 = cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake3 = cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake4 = cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')


add_extra_additives(cake1, ['strawberries', 'sugar-flowers'])
cake1.show_info()

add_extra_additives(cake2, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts'])
    
cake2.show_info()
