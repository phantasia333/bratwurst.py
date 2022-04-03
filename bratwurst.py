from time import sleep
import os

bw = 10   
bn = 8

people = int(input("People at cookout: "))
hd_pp = float(input("Hotdogs per person: "))

# bw = bratwurst (funnyword lol)
# bn = bun


needed = people * hd_pp # To calculate the amount of food needed, the program multiples the amount of people at the cookout by the amount of hotdogs that each person has.

def bratwurst(needed, hotdAvailable):  
    if needed % hotdAvailable == 0: # If the remainder of divided bratwursts totals 0... 
        bratwurst = needed / hotdAvailable # The total amount of bratwursts needed is divided by that which is available, otherwise...
    else:
        bratwurst = (needed // hotdAvailable) + 1 # One bratwurst (haha) is added to the total amount.

    return needed # The program then determines how much is needed into the console.

def leftovers(total, hotdAvailable, needed): # The amount of leftovers is determined by the total amount of bratwursts, the bratwursts available (hehe), and the bratwursts needed (i am the only one laughing rright now i think). 
    
    leftover = ((total * hotdAvailable) - needed)
    return leftover

bratwurstlol_packs = bratwurst(needed, bw)
wurstbuns = bratwurst(needed, bn)

bratwurst_remain  = leftovers(bratwurstlol_packs, bw, needed)
bratwurst_bun_remain  = leftovers(wurstbuns, bn, needed)

print("MINIMUM BRATWURST NEEDED: ", bratwurstlol_packs)
print("BRATWURST BUNS NEEDED LOL: ", wurstbuns)
print("REMAINING BRATWUWRST LOL:  ", bratwurst_remain)
print("REAMINING BRATWURST BUN :thumbs_up:: ", bratwurst_bun_remain)


sleep(5) 

print("sorry if that was annoying lol")

