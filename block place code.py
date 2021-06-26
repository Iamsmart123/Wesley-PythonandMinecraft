from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z= mc.player.getTilePos()
block = input("What is ID number?")
#block = (block)
#mc.setBlock(x,y,z,int(block))
mc.setBlock(x,y,z, int(block))

