"""
Player -玩家定义

玩家：
属性：昵称，手牌
方法：摸牌，整理

Author: Sizhuo Li
Date: 2023/7/10
"""
from Poker import Poker


class Player(object):
    def __init__(self, name):
        """
        初始化方法
        :param name:玩家姓名
        """
        self.name = name
        self.cards = []

    def __repr__(self):
        return self.display()

    def get(self, card):
        """
        摸牌
        :param card: 新增牌
        :return: no return
        """
        self.cards.append(card)

    def arrange(self):
        """
        整牌
        :return:no return
        """
        self.cards.sort()

    def display(self):
        return self.cards


def main():
    poker = Poker()
    poker.shuffle()
    PlayerNames = ['东邪', '西毒', '南帝', '北丐']
    players = [Player(t) for t in PlayerNames]
    for _ in range(1, 14):
        for p in players:
            card = poker.deal()
            p.get(card)
    for p in players:
        p.arrange()
        print(f'{p.name}: {p.display()}')


if __name__ == '__main__':
    main()
