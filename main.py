print("Welcome to Dhruv's Chemistry Calculator")
chem=str(input('Enter the calculation(no capital letters(single word)): '))

if(chem=='density'):
    mass=float(input('Enter the mass:'))
    volume=float(input('Enter the volume:'))
    density=mass/volume
    print('%0.3f is the density.' %(density))
if(chem=='molarity'):
    moles=float(input('Enter the moles of solute:'))
    liters=float(input('Enter the liters of solution:'))
    molarity=moles/liters
    print('%0.3f is the molarity' %(molarity))
