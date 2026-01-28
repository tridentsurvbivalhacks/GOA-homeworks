def user_contacts(data):
    _result = {
    
    }
    for info in data:
        if len(info) == 2:
            _result[info[0]] = info[1]
        else:
            _result[info[0]] = None
    return _result
print(user_contacts([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]))



def define_suit(card):
    _dict = {
        "D":"diamonds",
        "C":"clubs",
        "H":"hearts",
        "S":"spades"
    }
    for i in _dict:
        return _dict[card[1]]
print(define_suit("9S"))