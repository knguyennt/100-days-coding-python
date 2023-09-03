from player import Player
from dealer import Dealer
from const import MIN_POINT, MAX_POINT

def check_winner(player: Player, bot: Player):
    print('Bot points: ', bot.get_total_points())
    print('Player points: ', player.get_total_points())
    if (player.get_total_points() > MAX_POINT or player.get_total_points() < MIN_POINT):
        return 'Bot is the winner'
    
    elif (bot.get_total_points() > MAX_POINT or bot.get_total_points() < MIN_POINT):
        return 'Player is the winner'
    
    elif (bot.get_total_points() == player.get_total_points()):
        return 'Its a tie!!!!!'
    
    return 'Player is the winner' if player.get_total_points() > bot.get_total_points() else 'Bot is the winner'

if __name__ == '__main__':
    print('Welcome to the black jack game')
    dealer = Dealer()
    player = Player(dealer.deal())
    bot = Player(dealer.deal())

    while (True):
        if (bot.get_total_points() < MIN_POINT):
            bot.draw(dealer.draw())

        print('Your current hand is ', player.show_current_hand())
        print('You want to continue draw? : ')
        draw = input()
        if (draw.lower() != 'yes'):
            break

        player.draw(dealer.draw())

    winner = check_winner(player=player, bot=bot)

    print(winner)

