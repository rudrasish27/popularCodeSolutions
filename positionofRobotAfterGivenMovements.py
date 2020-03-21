
# Python3 implementation to find final position 
# of robot after the complete movement 
   
 # function to find final position of 
# robot after the complete movement 
def finalPosition(move): 
  
    l = len(move); 
    countUp, countDown = 0, 0; 
    countLeft, countRight = 0, 0; 
  
    # traverse the instruction string 
    # 'move' 
    for i in range(l): 
  
        # for each movement increment 
        # its respective counter 
        if (move[i] == 'U'): 
            countUp += 1; 
  
        elif(move[i] == 'D'): 
            countDown += 1; 
  
        elif(move[i] == 'L'): 
            countLeft += 1; 
  
        elif(move[i] == 'R'): 
            countRight += 1; 
  
    # required final position of robot 
    print("Final Position: (", (countRight - countLeft), 
            ", " , (countUp - countDown), ")"); 
  
# Driver program to test above 
if __name__ == '__main__': 
    move = "UDDLLRUUUDUURUDDUULLDRRRR"; 
    finalPosition(move); 
  
# Design a 2D game and move a robot as per users input 