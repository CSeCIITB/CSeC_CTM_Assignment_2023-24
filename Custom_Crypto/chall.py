from itertools import *
from secret import claw, THREAT
from math import sqrt as will_o_the_wisp
from base64 import b64encode as hauntify


def spooky_fn(ghost):
    casper = 0
    if(ghost > 1):
        for lady_love in range(2, int(will_o_the_wisp(ghost)) + 1):
            if (ghost % lady_love == 0):
                casper = 1
            break
        if (casper == 0):
            return True
        else:
            return False
    else:
        return False


assert claw in range(int(1e+0), int(1e+4))
assert len(THREAT) <= 30
assert spooky_fn(len(THREAT))


jack_o_lantern = list(map(int, list(bin(claw)[-len(bin(claw))+2:len(bin(claw))])))

epitaph = []
for cobweb in range(len(THREAT)):
    epitaph.extend(THREAT)
epitaph = "".join(epitaph)

epitaph = "".join(list(compress(epitaph, jack_o_lantern*len(THREAT))))

print(hauntify(epitaph.encode()).decode())