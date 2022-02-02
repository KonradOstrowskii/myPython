
class cake:

    bakery_offer = []
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self, name, kind, taste, additives, filling, __gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.gluten_free = __gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print("We can add text only at cake :")

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
        if self.gluten_free is False:
            print("Contains gluten")
        else:
            print("Gluten Free")
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print("*" * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    def __str__(self):
        return "{} - {} with {} filled with {}".format(self.kind, self.name, self.additives, self.filling)

    def __iadd__(self, other):
        if type(other) is str:
            self.additives.append(other)
            return self
        elif type(other) is list:
            self.additives.extend(other)
        else:
            raise Exception('sorry this operation is not implement')

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake1 = cake('Vannila Cake', 'cake', 'vanilla', [
             'vanilla', 'honey'], 'cream', False, 'Happy Birthday')
cake2 = cake('chockolate cake', 'cake', 'chockolate',
             'chockolate', 'nutella', False, '')
cake3 = cake('lemon cake', 'cake', 'lemon', 'lemon', '', False, '')
cake4 = cake('Super Sweet Maringue', 'meringue',
             'very sweet', [], '', False, 'ALOHA')
cake5 = cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, '')


print("Today in our offer:")
for c in cake.bakery_offer:
    c.show_info()

cake1.Text = 'Happy birthday!'
cake2.Text = '18'
cake5.Text = 'aloha'

for c in cake.bakery_offer:
    c.show_info()
