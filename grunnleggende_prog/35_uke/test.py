#x = bool(input("True eller False"))
#
#print(x) 

user_bool = None

while user_bool != "true" or user_bool != "false":
    user_bool = input("Skriv inn True eller False: ").lower()
    print(user_bool)
if user_bool == "true":
    user_bool = True
    print(f"verdien av user_bool={user_bool}") 
elif user_bool == "false":
    user_bool = False
    print(f"verdien av user_bool={user_bool}") 

#if user_bool == "true":
#    user_bool = True
#    print(f"verdien av user_bool={user_bool}") 
#elif user_bool == "false":
#    user_bool = False
#    print(f"verdien av user_bool={user_bool}") 
#else:
#    print("Kjenner ikke igjen verdi.")