import random
def check_sales_target():
    today_sales = random.randint(1000, 10000)  
    print(f"today sales are:{today_sales}")
    return today_sales
cuurent_sales=check_sales_target()
try:
    with open("file.txt","r") as f:
        content= f.read().strip()
        if (content == ""):
            previous_high_score=0
        else:
            previous_high_score=int(content)
except (ValueError,FileNotFoundError,FileExistsError):
    previous_high_score=0
    print(f"your previous highest sales are {previous_high_score} now checking and compairing TODAY and PREVIOUS score.....")
    
if cuurent_sales>previous_high_score:
    print(f"congrats today we got highest sales which are:{cuurent_sales} ")
    with open("file.txt","w") as f:
        f.write(str(cuurent_sales))
else:
    print(f"NO HIGH SCORE BROKEN because Previous high score {previous_high_score} remains the same and today's sales are {cuurent_sales}")
    
    
   
#data nikalte waqt text ko number (int()) banana parta hai taake maths ho sake, aur data vapas file mein dalte waqt number ko text (str()) banana parta hai taake file usay save kar sake!