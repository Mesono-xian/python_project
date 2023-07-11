"""
Poker -扑克定义

扑克：
属性：存52张牌（去掉大小王）的容器
方法：洗牌，发牌

Author: Sizhuo Li
Date: 2023/7/4
"""
import random
from Card import Card
from Card import Suit

class Poker(object):
    """
    扑克类
    """

    def __init__(self):
        self.cards = []  # 初始化空牌组
        self.counter = 0  # 计数器，便于发牌
        # 两次遍历，先遍历花色，后遍历点数
        for suit in Suit:
            for face in range(1, 14):
                card = Card(suit, face)  # 构造器语法构造单牌
                self.cards.append(card)
        """
        列表生成式语法可简化上述遍历如下：
        self.cards = [Card(suit, face) for suit in Suit for face in range(1, 14)]
        """

    def __repr__(self):
        return self.deal()

    def shuffle(self):
        """
        洗牌
        :return: no return
        """
        counter = 0  # 计数器清零
        random.shuffle(self.cards)

    def deal(self):
        """
        发牌
        :return:每张发出去的牌
        """
        card = self.cards[self.counter]
        self.counter += 1
        return card

    def check(self):
        """
        检查牌是否发完(bool类型)
        :return: 没发完1，发完0
        """
        return self.counter < len(self.cards)


def main():
    poker = Poker()
    poker.shuffle()
    while poker.check():
        print(poker.deal(), end=' ')


if __name__ == '__main__':
    main()
