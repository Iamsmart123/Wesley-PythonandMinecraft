from mcpi.minecraft import Minecraft as mcs
import random
mc = mcs.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    num = random.randint(1,4)
    if num ==1:
        mc.setBlocks(x,y,z,x+4,y,z,2)
        # red
        x=x+4
    elif num == 2:
        mc.setBlocks(x,y,z,x-4,y,z,2)
        x=x-4
    elif num == 3:
        mc.setBlocks(x,y,z,x,y,z+4,2)
        z=z+4
    else:
        mc.setBlocks(x,y,z,x,y,z-4,2)



