from NewCmdCode import playerlist
from colored import attr

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

def showcard(description):

    print(bordered(description))
## Chance Cards
def GoToJail(player):
    player.position = 10
    player.injail = True
    print(bordered(" Yeet\n" + bordered("yeet")))

GoToJail(playerlist[0])
