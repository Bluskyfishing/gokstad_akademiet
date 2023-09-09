#x = bool(input("True eller False"))
#
#print(x) 


#user_bool = None
#
#while user_bool != "true" or user_bool != "false":
#    user_bool = input("Skriv inn True eller False: ").lower()
#    print(user_bool)
#if user_bool == "true":
#    user_bool = True
#    print(f"verdien av user_bool={user_bool}") 
#elif user_bool == "false":
#    user_bool = False
#    print(f"verdien av user_bool={user_bool}") 

#if user_bool == "true":
#    user_bool = True
#    print(f"verdien av user_bool={user_bool}") 
#elif user_bool == "false":
#    user_bool = False
#    print(f"verdien av user_bool={user_bool}") 
#else:
#    print("Kjenner ikke igjen verdi.")

#spiller_score = 0
#pc_score = 0
#runder = 0
#
#valg_navn = ["stein", "saks", "papir"]
#
#while runder < 10:
#    pc_valg = random.randint(0, 2)
#    spiller_valg = int(input("Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))
#
#    print(f"Spiller valgte: {valg_navn[spiller_valg]}")
#    print(f"PC valgte: {valg_navn[pc_valg]}")
#
#    if spiller_valg == pc_valg:
#        print("Uavgjort!")
#    elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
#        spiller_score += 1
#        print(f"Spiller vinner!\nScore: Spiller: {spiller_score} PC: {pc_score}")
#    else:
#        pc_score += 1
#        print(f"PC vinner!\nScore: Spiller: {spiller_score} PC: {pc_score}")
#
#    runder += 1
#
#print("Spillet er ferdig!")
#

#import random
#
#liste = []
#
#
#
#for i in range(0,5):
#    randomtall = random.randint(0,100)
#    liste.append(randomtall)
#
#print(liste)

from tkinter import *

def valg_stein():
    spiller_valg = 0 
def valg_saks():
    spiller_valg = 1 
def valg_papir():
    spiller_valg = 2

runder = 0
spiller_score = 1
pc_score = 2 


root = Tk()
root.title("Stein, saks, papir spill")
root.geometry("1000x1000")


var = StringVar()
var.set("Runde:")
label = Label(root, textvariable=var)
label.pack()
ny_runde = "Runde:",runder
var.set(ny_runde)


#var = StringVar()
#var.set("Spiller Score:")
#label2 = Label(root, textvariable=var)
#label2.pack()
#spiller_score_update = "Spiller_score:",spiller_score
#var.set(spiller_score_update)
#
#var = StringVar()
#var.set("PC Score:")
#label3 = Label(root, textvariable=var)
#label3.pack()
#pc_score_update = "PC_score:",pc_score
#var.set(pc_score_update)


stein_btn = PhotoImage(file="stein.png")
scaled_stein_image = stein_btn.subsample(2, 2)
my_button = Button(root, image=scaled_stein_image, command=valg_stein)
my_button.pack(pady=10)

saks_btn = PhotoImage(file="saks.png")
scaled_saks_image = saks_btn.subsample(3, 3)
my_button2 = Button(root, image=scaled_saks_image, command=valg_saks)
my_button2.pack(pady=10)

papir_btn = PhotoImage(file="papir.png")
scaled_papir_image = papir_btn.subsample(2, 2)
my_button3 = Button(root, image=scaled_papir_image, command=valg_papir)
my_button3.pack(pady=10)




root.mainloop()