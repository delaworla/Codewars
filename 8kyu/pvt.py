

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    num = (given_mass1/molar_mass1 + given_mass2/molar_mass2) * (temp + 273.15) * 0.082
    return num / volume
    
    # your code goes here