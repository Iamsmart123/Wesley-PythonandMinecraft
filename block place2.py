from mcpi.mincraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
width = 5
height = 5
lenght = 5
block = 20
air = 0
mc.setBlock(x,y,z,x+width,y+height,z+lenght,block)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+lenght-1,air)

