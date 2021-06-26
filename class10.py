from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
from random import randint
x,y,z = mc.player.getPos()
com = randint(0,16) #computer answer
print("com = ",com)
for i in range(5):
    for j in range(5):
        num = randint(0,16)
        mc.setBlock(x+i,y,z+j,35,num)
while True:
    hits= mc.event.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos) #color data
        data = block.data
        print("data = ",data)
        if data == com:
            mc.postToChat("you win >-<")
            break
        elif data < com:
            mc.postToChat("you answer < com")
        else:
            mc.postToChat("you answe > com")

