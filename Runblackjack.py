mydeck = Backjack.Deck()
mydeck.Shuffle()
myplayer = Backjack.Player()
name = myplayer.Playername()
mydeck.show()
myplayer.hand = []


def playgame(myplayer, mydeck):
    totalCards = len(mydeck)
    myhand = myplayer.draw(mydeck)
    player_deck_len = len(myplayer)
    myplayer.showhand()
    my_bet = Backjack.Bet(myplayer.placeBet())
    my_bet.totalChips()
    total = myplayer.totalhandvalue()
    print(f"The total value of your cards is {total}")
    userInput = input("Do you want to take card (Y/N): \n")
    if userInput.lower() == 'y':
        while userInput == 'y' and total < 21:
            myhand = myplayer.drawone(mydeck)
            player_deck_len = len(myplayer)
            print(f"{name} you have {player_deck_len} cards with you and they are :")
            myplayer.showhand()
            total = myplayer.totalhandvalue()
            print(f"The total value of your cards is {total}")
            userInput = input("Do you want to continue to take card(Y/N): \n")
            if total == 21:
                print(f"{name}-You won")
                break
            elif total>21:
                print(f"{name} - you got busted")
                break

    elif userInput.lower() == 'n':
        mydealer = Backjack.dealer('comp')
        totalCards = len(mydeck)
        mydealerhand = mydealer.dealerdraw(mydeck)
        mydealer.showdealer()
        total1 = mydealer.totalhandvalue()
        while total1 < 21:
            mydealerhand = mydealer.dealerdrawone(mydeck)
            mydealer.showdealer()
            total1 = mydealer.totalhandvalue()
            if total1 == 21:
                print("Dealer won")
                break
        print(f"dealer got busted. {name} won")

    len(mydeck)

playgame(myplayer, mydeck)
