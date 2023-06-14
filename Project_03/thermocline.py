'''Abdullah Shahzad
9/22/2021
CS 152 B
Project_03'''

'''This program will compute the thermocline in Great Pond for July 2019'''


def density(temps):
    '''This function converts temperatures to density'''
    rho = [] #empty list to hold all the calculated density values
    
    for temp in temps: #for loop to loop over all temperature values in temps
        temp2rho = 1000 * (1 - (temp + 288.9414) * (temp - 3.9863)**2 / (508929.2*(temp + 68.12963))) #equation to convert temp to density
        rho.append(temp2rho) #appends calculated density to the list rho[]
    return rho #returns the list
    #END OF FUNCTION

def thermocline_depth(temps, depths):
    '''This function computes the derivative of the density with respect to depth'''
    rhos = density(temps) #rhos is assigned the result of calling density with the argument temps
    drho_dz = [] #drho_dz is assigned an empty list

    for i in range(len(rhos)-1): #for loop with variable i in range 1 less than the length of rhos
        drho_dz.append((rhos[i+1] - rhos[i])/(depths[i+1] - depths[i])) #appends the derivative of rhos with respect to depths to drho_dz

    max_drho_dz = -1.0 #assigning a variable
    maxindex = -1 #also assigning a variable

    for i in range (len(drho_dz)): #for loop for i in range (the length of drho_dz)
        if drho_dz[i] > max_drho_dz: #conditional checking if drho_dz with index i is greater than max_drho_dz
            max_drho_dz = drho_dz[i] #assigns drho_dz to max_drho_dz if conditional evaluates to true
            maxindex = i #assigns i to maxindex if conditional evaluates to true

    thermoDepth = (depths[maxindex] + depths[maxindex+1]) / 2 #assignment of thermoDepth
    return thermoDepth #the function returns thermoDepth

