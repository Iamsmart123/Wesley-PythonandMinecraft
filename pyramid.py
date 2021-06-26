from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
def build(x,y,z,base):
    heigth=(base//2)+1
    for i in range(heigth):
        x1=x+i
        y1=y+i
        z1=z+i
        x2 = x+base-i
        z2 = z+base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,24)
x,y,z=mc.player.getTilePos()
base=int(input())
build(x,y,z,base)        

