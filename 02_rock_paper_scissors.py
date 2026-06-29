import random
computer = random.choice([-1,0,1])
user_input = input("enter a choice from R,P,S: ").lower()
if(user_input not in ["r", "p", "s"]):
    print("wrong approach : 'invalid input', please enter a valid input")
    exit()
else:
    print("valid input, starting the game")
user_dict =  {"r":-1 , "p":0 , "s":1}
reverse_user_dict= { -1:"rock" , 0:"paper" , 1:"scissors"} 
input_converted_to_num= user_dict[user_input]

print(f"you chose: {user_input} which is({reverse_user_dict[input_converted_to_num]}) and computer chose ({reverse_user_dict[computer]})")

if (input_converted_to_num == computer):
    print("draw")

else:
    
    if (computer == -1 and input_converted_to_num == 1):
        print("YOU WINNNN !!!!")
        
        
    elif(computer == -1 and input_converted_to_num == 0):
       print("YOU LOST :(")
       
    elif(computer == 1 and input_converted_to_num == -1):
       print("YOU LOST :(")
       
    elif(computer == 1 and input_converted_to_num == 0):
       print("YOU WINNNN !!!!")
       
    elif(computer == 0 and input_converted_to_num == -1):
       print("YOU WINNNN !!!!")
       
    elif(computer == 0 and input_converted_to_num == 1):
        print("YOU LOST :(")
        
        
    else:
        print("something went wrong")