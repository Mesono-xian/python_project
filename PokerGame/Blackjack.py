"""
Blackjack -21点游戏

Author: Sizhuo Li
Date: 2023/7/11
"""

from Poker import Poker
from Player import Player
from enum import Enum


class Jack(Enum):
    jack = 21


def ACheck(who):
    if who + 11 <= Jack.jack.value:
        who += 11
    else:
        who += 1
    return who


def Calculate(count, card):
    if card.face == 2 or card.face == 3 or card.face == 4 or card.face == 5 or card.face == 6:
        count += 1
    elif card.face == 7 or card.face == 8 or card.face == 9:
        count += 0
    else:
        count -= 1
    return count


def main():
    poker = Poker()
    poker.shuffle()
    player = Player('玩家')
    dealer = Player('庄家')
    player_score = 0
    dealer_score = 0
    high_low = 0
    for i in range(2):
        card = poker.deal()
        high_low += Calculate(high_low, card)
        player.cards.append(card)
        if card.face == 1:
            player_score = ACheck(player_score)
        else:
            player_score += card.value
        card = poker.deal()
        high_low += Calculate(high_low, card)
        dealer.cards.append(card)
        if card.face == 1:
            dealer_score = ACheck(dealer_score)
        else:
            dealer_score += card.value
    print(f'玩家手牌：{player.cards},当前得分：{player_score}')
    print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
    print('------------')
    flag1 = 1
    flag2 = 1
    while poker.check():
        if flag1 == 1:
            card = poker.deal()
            choice = input('要牌(Y) 或 停牌(N)')
            if choice == 'Y':
                player.cards.append(card)
                high_low += Calculate(high_low, card)
                if card.face == 1:
                    player_score = ACheck(player_score)
                else:
                    player_score += card.value
                print(f'玩家手牌：{player.cards},当前得分：{player_score}')
                print('------------')
                if player_score == Jack.jack.value:
                    print('玩家获胜')
                    return 0
                elif player_score > Jack.jack.value:
                    print('玩家爆牌，庄家获胜')
                    return 0
            elif choice == 'N':
                print(f'玩家手牌：{player.cards},当前得分：{player_score}')
                print('------------')
                flag1 = 0
            else:
                print('选项输入不合法，请重新输入')
                print('------------')
        if flag2 == 1:
            card = poker.deal()
            if dealer_score < 17 or high_low < 0:
                dealer.cards.append(card)
                high_low += Calculate(high_low, card)
                if card.face == 1:
                    dealer_score = ACheck(dealer_score)
                else:
                    dealer_score += card.value
                print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
                print('------------')
                if dealer_score == Jack.jack.value:
                    print('庄家获胜')
                    return 0
                elif dealer_score > Jack.jack.value:
                    print('庄家爆牌，玩家获胜')
                    return 0
            else:
                print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
                print('------------')
                flag2 = 0

    if player_score > dealer_score:
        print(f'玩家手牌：{player.cards},当前得分：{player_score}')
        print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
        print('玩家胜')
    elif player_score < dealer_score:
        print(f'玩家手牌：{player.cards},当前得分：{player_score}')
        print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
        print('庄家胜')
    else:
        print(f'玩家手牌：{player.cards},当前得分：{player_score}')
        print(f'庄家手牌：{dealer.cards},当前得分：{dealer_score}')
        print('平局')


if __name__ == '__main__':
    main()
