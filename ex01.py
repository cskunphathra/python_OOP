class Tree:
    def __init__(self, height, width, generated_money):
        self.height = height
        self.width = width
        self.generated_money = generated_money

    def feed_A(self):
        self.generated_money = self.generated_money - 10
        self.width = self.width + 12

    def feed_B(self):
        self.generated_money = self.generated_money - 8
        self.height = self.height + 10


    def sell(self):
        self.generated_money = self.generated_money + self.width * self.height ** 0.8
        print('Width =', self.width, 'Heigth =', self.height )
        print('Generated_money =' , self.generated_money)

tree_A = Tree(10, 10, 1000)
tree_A.feed_A()
tree_A.feed_B()
tree_A.sell()

tree_B = Tree(23, 8 ,254)
tree_B.feed_B()
tree_B.sell()

tree_C = Tree(300, 14, 850)
tree_C.feed_A()
tree_C.sell()