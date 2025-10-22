def to_celsius(f):
    return 5/9 * (f - 32)
print(to_celsius(222))


#2)sum all parameters <3
# def calculate_damage(opening_attack, core_damage, finishing_move):
# ---> "wizzard new life is SUMED_CALCULATED"
# calculate_damage(10, 20, 30)
def calculate_damage(opening_attack, core_damage, finishing_move): #defined(created) a function called "calculate_damage" with 3 parameters in it
    return f"wizzard new life is {opening_attack + core_damage + finishing_move}" # returned text with f string and used the parameters to calculate the damage 
print(calculate_damage(10,20,30)) #calculated the damage by giving the parameteres value and printing out the results in terminal