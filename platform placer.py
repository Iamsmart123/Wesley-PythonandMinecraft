from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos()
for i in range(100000000000000000):
    mc.setBlock(x+i,y,z+i,46)
