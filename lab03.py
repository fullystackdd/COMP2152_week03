import random

# Dice Options using list() and range()
diceOptions = list(range(1, 7))

#Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons)) 

# Inputs combat strength hero 
combatStrength = int (input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength must be between 1 and 6.")
    combatStrength = 1 #Default value for invalid input

# Inputs combat strength for monster

mCombatStrength =  int(input("Enter Monster's combat strength (1-6): "))
if mCombatStrength < 1 or combatStrength > 6:
    print("Invalid input! Monster combat strength must be between 1 and 6.")
    mCombatStrength = 1 #Default value for invalid input


#Simulate Battle rounds
    for j in range(1, 21, 2): #Simulation of 20 seconds, stepping by 2
    #Dice rolls for hero and monster
        heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

 
    #Calculate the weapons strength
    heroWeapon = weapons[heroRoll -1 ]
    monsterTotal = weapons[monsterRoll - 1]

       #Calculate total Strength
heroTotal = combatStrength + heroRoll
monsterTotal = combatStrength + monsterRoll

    #Print round details
print(f"\nRound {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
print(f"Hero selected: {heroTotal}, Monster selected: {monsterTotal}")
print(f"Hero total strenght: {heroRoll}, Monster total strength: {monsterTotal}")

#Determine  winner
if heroTotal > monsterTotal:
    print("Hero wins the round!")
elif heroTotal < monsterTotal:
    print("Monster wins the round!")
else:   
    print("It's a tie!")

    if j == 11:
        print("\n Battle Truce declared in Round 11. Game Over!")
        break
    if j != 11:
        print("\n Battle continues...")