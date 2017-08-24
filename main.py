-
import random
from cards import Card
from method import *
#其实更好的方法是，import method ，然后通过method.XXX()去调用函数呢

deck = []
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        new_card = Card(suit_id, rank_id)
        if new_card.rank_id == 8:
            new_card.value = 50
        deck.append(new_card)
up_card = random.choice(deck)
deck.remove(up_card)
active_suit = up_card.suit
p_hand = []
for a in range(1,6):
    a = random.choice(deck)
    p_hand.append(a)
    deck.remove(a)
print "\nYour hand:"
for card in p_hand:
    print card.short_name,
print "  Up card: ", up_card.short_name
print "active_suit: ",active_suit
print "What would you like to do?"

response = raw_input("Type a card name or 'Draw' to take a card: ")
## play or draw a card
valid_play = False
while not valid_play:
    selected_card = None
    while selected_card == None:
        if response.lower() == 'draw':
            valid_play = True
            if len(deck) > 0:
                card = random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print "You drew", card.short_name
            else:
                print "There are no cards left in the deck"
                blocked += 1
            break
        else:
            for card in p_hand:
                if response.upper() == card.short_name:
                    selected_card = card
            if selected_card == None:
                response = raw_input("You don't have that card. Try again:")
            if selected_card.rank == '8':
                valid_play = True
                is_eight = True
            elif selected_card.suit == active_suit:
                valid_play = True
            elif selected_card.rank == up_card.rank:
                valid_play = True
            if not valid_play:
                response = raw_input("That's not a legal play. Try again: ")
c_hand = []
blocked = 0
done = False
p_total = c_total = 0
while not done:
    #__init__cards()
    #card = Card(suit_id, rank_id)
    game_done = False
    while not game_done:
        blocked = 0
        player_turn()
        get_new_suit()
        if len(p_hand) == 0:
            game_done = True
            print
            print "You won !"
        if not game_done:
            computer_turn()
            get_new_suit()
        if len(c_hand) == 0:
            game_done = True
            print
            print "Computer won! "
            #display the game score here
        c_points = 0
        for card in p_hand:
             c_points += card.value
        c_total += c_points
        print "Computer got %i points for your hand" % c_points
    if blocked >= 2:
        game_done = True
        print "Both player blocked, GAME OVER."
        player_points = 0
        for card in c_hand:
            p_points += card.value
        p_total += p_points
        c_points = 0
        for card in p_hand:
            c_point += card.value
        c_total += c_points
        print "You got %i points for computer's hand" % p_points
        print "Computer got %i points for your hand" % c_points


    play_again = raw_input("play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print "\nSo far,you have %i points" % p_total
        print "and the computer has %i points.\n" % c_total
    else:
        done = True
print "\n Final Score:"
print "You: %i       Computer: %i" %(p_total, c_total)



