# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:12:12 2018

@author: dlekk
"""
import random
from colorama import init
init()
from colorama import Fore, Style

characters = ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ', 'K ',
              'L ', 'M ', 'N ', 'O ', 'P ','Q ', 'R ', 'S ', 'T ', 'U ', 'V ',
              'W ', 'X ', 'Y ', 'Z ', '~ ', '@ ', '# ', '$ ', '% ', '^ ', '& ',
              '* ', '= ', '+ ', ': ','; ', '< ', '> ', '/ ']

used_characters = []

print '~PROGRAM INITIALIZED~', '\n'
print 'FRIPPLESQUARED (v1.1)'
print '[Conceived and coded by Damien Lekkas (c) 2018]', '\n'

print '+----------------------------INSTRUCTIONS--------------------------------+'
print '|                                                                        |' 
print '| FrippleSquared is a game of memory. Select numbers from Board A and    |'
print '| Board B to find the matching characters. Each character will appear    |'
print '| once in Board A and once in Board B. Players will take turns selecting |'
print '| one number from each board and will be awarded a point for each match  |'
print '| found. The game ends once all matches are found and the boards are     |'
print '| cleared. The player with the higher number of matches found is the     |'
print '| winner.                                                                |'
print '|                                                                        |'
print '+------------------------------------------------------------------------+', '\n'                                  

print 'The boards will now be randomly generated...', '\n'
raw_input('Press enter to begin: ')                                  
print '\n'
#-----------------BOARD RANDOMIZATION AND INITIALIZATION-----------------------

fripple_board_A = 5*[[] for x in range(5)]
fripple_board_B = 5*[[] for y in range(5)]

empty_fripple_A = 5*[[] for x in range(5)]
empty_fripple_B = 5*[[] for y in range(5)]

for cell in range(25):
    fripple_board_A[cell] = characters[random.randint(0, len(characters)-1)]        
    characters.remove(fripple_board_A[cell])        
    used_characters.append(fripple_board_A[cell])

for cell in range(25):
    fripple_board_B[cell] = used_characters[random.randint(0, len(used_characters)-1)]
    used_characters.remove(fripple_board_B[cell])

for cell in range(9):
    empty_fripple_A[cell] = '0' + str(cell + 1)
    empty_fripple_B[cell] = '0' + str(cell + 1)               

for cell in range(9,25):
    empty_fripple_A[cell] = str(cell + 1)
    empty_fripple_B[cell] = str(cell + 1)  

p1_score = 0
p2_score = 0

#-----------------------FUNCTION TO GENERATE ANSWERS---------------------------
def boardkey():        
    xAB = 0
    yAB = 5
    for row in range(5):
        print ' | '.join(fripple_board_A[xAB:yAB]), '\t'*2, ' | '.join(fripple_board_B[xAB:yAB])
        print '---------------------', '\t'*2, '---------------------'
        xAB += 5
        yAB += 5
    print '        BOARD A        ', '\t'*2, '        BOARD B        '

#-------------------FUNCTION TO GENERATE GUESSING BOARDS-----------------------
def guessboard():
    xE = 0
    yE = 5
    print '\t'*3, '-----------------------', '\t', '-----------------------'
    for row in range(5):
        print '\t'*3, ' | '.join(empty_fripple_A[xE:yE]), '\t'*2, ' | '.join(empty_fripple_B[xE:yE])
        print '\t'*3, '-----------------------', '\t', '-----------------------'
        xE += 5
        yE += 5        
    print '\t'*3, '       BOARD A       ', '\t'*2, '       BOARD B       '

guessboard()
print '\n'

solved_A = []
solved_B = []

#-----------------------------GAME LOOP----------------------------------------
while p1_score + p2_score != 25:
    
#-------------------------- PLAYER 1 PHASE-------------------------------------
    p1_flag = True    
    while p1_flag == True: 
        print Fore.CYAN + '--PLAYER 1--' + Style.RESET_ALL, '\n'
        
        while True:
            try:
                p1_guess_A = raw_input('Select a tile to overturn on Board A (1-25): ')
                p1_guess_A = int(p1_guess_A)
                p1_guess_B = raw_input('Select a tile to overturn on Board B (1-25): ')
                p1_guess_B = int(p1_guess_B)
                break
            except ValueError:
                print '\n', 'That is not a number! Please enter numbers only!'
        
        checkpass = False
        while checkpass == False:    
            if p1_guess_A not in range(1,26) or p1_guess_B not in range(1,26):
                print '\n', 'That is an invalid number! Enter an appropriate number in range (1-25)!', '\n'
                p1_guess_A = input('Select a tile to overturn on Board A (1-25): ')
                p1_guess_B = input ('Select a tile to overturn on Board B (1-25): ')
           
            elif empty_fripple_A[p1_guess_A-1] in solved_A or empty_fripple_B[p1_guess_B-1] in solved_B:
                print '\n' 'That tile was already solved! Select an unsolved tile!', '\n'
                p1_guess_A = input('Please select a tile to overturn on Board A (1-25): ')
                p1_guess_B = input('Please select a tile to overturn on Board B (1-25): ')
              
            else:
                checkpass = True
        
        print '\n'
        empty_fripple_A[p1_guess_A-1] = Fore.YELLOW + fripple_board_A[p1_guess_A-1] + Style.RESET_ALL 
        empty_fripple_B[p1_guess_B-1] = Fore.YELLOW + fripple_board_B[p1_guess_B-1] + Style.RESET_ALL
        guessboard()

        if empty_fripple_A[p1_guess_A-1] == empty_fripple_B[p1_guess_B-1]:
            empty_fripple_A[p1_guess_A-1] = Fore.CYAN + fripple_board_A[p1_guess_A-1] + Style.RESET_ALL 
            empty_fripple_B[p1_guess_B-1] = Fore.CYAN + fripple_board_B[p1_guess_B-1] + Style.RESET_ALL
            
            solved_A.append(empty_fripple_A[p1_guess_A-1])
            solved_B.append(empty_fripple_B[p1_guess_B-1])
            
            p1_score += 1
            print '\n', 'PLAYER 1 MATCH!', '\n'
            print '+1 POINT', '\n'
            
            if p1_score + p2_score != 25:
                raw_input('Press ENTER to take another turn: ')
                print '\n'
                guessboard()
                print '\n'
       
            else:
                break
         
        else:
            if len(str(p1_guess_A)) == 2:
                empty_fripple_A[p1_guess_A-1] = str(p1_guess_A) 
            elif len(str(p1_guess_A)) == 1:
                empty_fripple_A[p1_guess_A-1] = '0' + str(p1_guess_A)
            
            if len(str(p1_guess_B)) == 2:
                empty_fripple_B[p1_guess_B-1] = str(p1_guess_B) 
            elif len(str(p1_guess_B)) == 1:
                empty_fripple_B[p1_guess_B-1] = '0' + str(p1_guess_B)
            
            print '\n', 'MISMATCH!', '\n' 
            p1_flag = False
    
    if p1_score + p2_score == 25:
        break
    
    else:
        raw_input('Press enter for Player 2 turn: ')        
    
    print '\n'
    guessboard()
    print '\n'
    
#-----------------------------PLAYER 2 PHASE-----------------------------------    
    p2_flag = True
    while p2_flag == True:
        print Fore.MAGENTA + '--PLAYER 2--' + Style.RESET_ALL, '\n'
        
        while True:
            try:
                p2_guess_A = raw_input('Select a tile to overturn on Board A (1-25): ')
                p2_guess_A = int(p2_guess_A)
                p2_guess_B = raw_input('Select a tile to overturn on Board B (1-25): ')
                p2_guess_B = int(p2_guess_B)
                break
            except ValueError:
                print '\n', 'That is not a number! Please enter numbers only!'
        
        checkpass = False
        while checkpass == False:    
            if p2_guess_A not in range(1,26) or p2_guess_B not in range(1,26):
                print '\n', 'That is an invalid number! Enter an appropriate number in range (1-25)!', '\n'
                p2_guess_A = input('Select a tile to overturn on Board A (1-25): ')
                p2_guess_B = input ('Select a tile to overturn on Board B (1-25): ')
            
            elif empty_fripple_A[p2_guess_A-1] in solved_A or empty_fripple_B[p2_guess_B-1] in solved_B:
                print '\n' 'That tile was already solved! Select an unsolved tile!', '\n'
                p2_guess_A = input('Please select a tile to overturn on Board A (1-25): ')
                p2_guess_B = input('Please select a tile to overturn on Board B (1-25): ')
                
            else:
                checkpass = True
    
        print '\n'
        empty_fripple_A[p2_guess_A-1] = Fore.YELLOW + fripple_board_A[p2_guess_A-1] + Style.RESET_ALL
        empty_fripple_B[p2_guess_B-1] = Fore.YELLOW + fripple_board_B[p2_guess_B-1] + Style.RESET_ALL
        guessboard()

        if empty_fripple_A[p2_guess_A-1] == empty_fripple_B[p2_guess_B-1]:
            empty_fripple_A[p2_guess_A-1] = Fore.MAGENTA + fripple_board_A[p2_guess_A-1] + Style.RESET_ALL
            empty_fripple_B[p2_guess_B-1] = Fore.MAGENTA + fripple_board_B[p2_guess_B-1] + Style.RESET_ALL
            
            solved_A.append(empty_fripple_A[p2_guess_A-1])
            solved_B.append(empty_fripple_B[p2_guess_B-1])
            
            p2_score += 1
            print '\n', 'PLAYER 2 MATCH!', '\n'
            print '+1 POINT', '\n'
            
            if p1_score + p2_score != 25:
                raw_input('Press ENTER to take another turn: ')
                print '\n'
                guessboard()
                print '\n'
       
            else:
                break
         
        else:
            if len(str(p2_guess_A)) == 2:
                empty_fripple_A[p2_guess_A-1] = str(p2_guess_A) 
            elif len(str(p2_guess_A)) == 1:
                empty_fripple_A[p2_guess_A-1] = '0' + str(p2_guess_A)
            
            if len(str(p2_guess_B)) == 2:
                empty_fripple_B[p2_guess_B-1] = str(p2_guess_B) 
            elif len(str(p2_guess_B)) == 1:
                empty_fripple_B[p2_guess_B-1] = '0' + str(p2_guess_B)
            
            print '\n', 'MISMATCH!', '\n'
            p2_flag = False
    
    if p1_score + p2_score == 25:
        break
    
    else:
        raw_input('Press enter for Player 1 turn: ')        
    
    print '\n'
    guessboard()
    print '\n' 
    
#------------------------------GAME OVER---------------------------------------    
print 'CONGRATULATIONS YOU CLEARED THE BOARDS!', '\n'
print 'FINAL SCORE:', str(p1_score), '-', str(p2_score), '\n'

if p1_score > p2_score:
    print 'PLAYER 1 WINS', '\n'
else:
    print 'PLAYER 2 WINS', '\n'
                                     
print 'Thanks for playing!', '\n'

raw_input('Press ENTER to exit: ')    

print '\n' '~PROGRAM TERMINATED~'          