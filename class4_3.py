from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
while True: 
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y+1,z,145)
    time.sleep(3)