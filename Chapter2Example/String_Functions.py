string = 'MinJae is science'
toCapital = string.capitalize()
print(toCapital)
doTitle = string.title()
doUpper = string.upper()
dolower = doUpper.lower()
doSwitch = dolower.swapcase()
print(doTitle + '\n' + doUpper + '\n' + dolower + '\n' + doSwitch+'\n')
print('The first String : ' +string)
#########################
print('@'+string.center(50)+'@\n@')
print(string.ljust(50)+'@\n@')
print(string.rjust(50)+'@\n')
