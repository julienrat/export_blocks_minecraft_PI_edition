# export minecraft stone blocks in to STL file, This is beta version version,
# It's use only one processor and very long ....
# Under CC by SA licence 
# Enjoy ! Julien Rat 


from mcpi.minecraft import Minecraft
block_size=4*4
file = open("export.scad", "w")
mc= Minecraft.create()
mc.postToChat("Export blocks")
x_player, z_player, y_player = mc.player.getPos()
print(x_player)
print(y_player)
print(z_player)
print("======")
for x_block in range (-4,4):
    for y_block in range (-4,4):
        for z_block in range (0,8):
            block_value = mc.getBlock(x_player+x_block,z_player+z_block,y_player+y_block)
            if (block_value==4):
                print("cube([",x_block,",",y_block,",",z_block,"]);")
                output = "translate(["+str(x_block)+","+str(y_block)+","+str(z_block)+"])"+"cube(1.00001,1.00001,1.00001)"+";"+"\n"
                file.write(output)
            

file.close()
mc.postToChat("fin d'exportation")
