import art

def find_max_bidder(auction_guest):
    re = -1
    name = ''
    for guest in auction_guest:
        if auction_guest[guest] > re:
            re = auction_guest[guest]
            name = guest
    return name

def blind_auction():
    auction_guest = {}
    while True:
        re = input("Do you want to bid? (y/n)")
        if re == 'n':
            break
        auction_name = input("Please type your name: ")
        auction_bid = input("Please input your bid: ")
        auction_guest[auction_name] = int(auction_bid)
    
    max_bidder = find_max_bidder(auction_guest)
    print(max_bidder)

if __name__ == "__main__":
    print(art.logo)
    blind_auction()