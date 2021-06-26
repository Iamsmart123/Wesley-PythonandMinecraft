from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z,= mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"hi","Person",\
           "","fghj")

