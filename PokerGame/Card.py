"""
Card -牌定义

牌：
属性：花色，点数
方法：显示牌面

Author: Sizhuo Li
Date: 2023/7/4
"""
from enum import Enum


class Suit(Enum):
    Spade, Heart, Club, Dimond = range(4)


class Card(object):
    """
    牌类
    """

    def __init__(self, suit, face):
        """
        初始化方法
        :param suit: 花色
        :param face: 点数
        """
        self.suit = suit
        self.face = face
        if self.face == 10 or self.face == 11 or self.face == 12 or self.face == 13:
            self.value = 10
        elif self.face == 1:
            pass
        else:
            self.value = self.face

    def __repr__(self):
        return self.display()

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.face < other.face
        return self.suit.value < other.suit.value

    def display(self):
        """
        显示牌面
        :return:对应牌面
        """
        suit = ['♠', '♥', '♣', '♦']
        face = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suit[self.suit.value]}{face[self.face]}'


def main():
    card1 = Card(Suit.Dimond, 13)
    print(card1)


if __name__ == '__main__':
    main()
