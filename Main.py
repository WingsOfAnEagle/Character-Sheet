import sys

menu_main = ['Create new character(1)', 'Saved characters(2)', 'Exit(3)']
loop = True 

while loop:
    print('\n'.join(menu_main))

    selection = int(input('\n\n\nEnter choice here: '))

    match selection:
        case 1:
            print('hello')
            break               
        case 2:
            print('hi')
            break       
        case 3:
            print('hey')    
            loop = False
            break
