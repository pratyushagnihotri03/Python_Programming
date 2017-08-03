class Mario():
    def move(self):
        print('I am moving!')


class Shroom():
    def eat_shroom(self):
        print('Now I am big!')


class BigMario(Mario, Shroom):
    pass # It is used to avoid syntax error because if there is no method is defined for this class.


bm = BigMario()
bm.move()
bm.eat_shroom()