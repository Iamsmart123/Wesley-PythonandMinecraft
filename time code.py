from mcpi.minecraft import Minecraft as mcs 
mc = mcs.create()
from time import sleep 
while True:
    mc.executeCommand("time add 50")
    sleep(0.1)
