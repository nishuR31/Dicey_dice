import random as r
import colorama as c
while True:     
   print(f"{c.Fore.YELLOW}1{c.Fore.RESET}:roll the dice\n{c.Fore.YELLOW}0:{c.Fore.RESET}exit")    
   user = input(f"{c.Fore.BLUE}what you want to do:")
   try:    
      if user=="1":         
         number = r.randint(1,6)         
         print(f"\n{c.Fore.RESET}rolled number:{c.Fore.GREEN}{number}")     
      elif user=="0": 
         print(f"\n{c.Fore.LIGHTCYAN_EX}Exiting.")        
         quit()
      else:
         raise ValueError (f"\n{c.Fore.RED} enter valid choice")
   except Exception as e:
      print(f"\n{c.Fore.RED} Error occured{c.Fore.RESET}")
      