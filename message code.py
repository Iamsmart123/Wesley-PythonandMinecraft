from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
username = input("blah blah blah")
message = input("what is your message?")
mc.postToChat()("<"+username+">"+message)
