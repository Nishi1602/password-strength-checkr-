import string 
import getpass

def check_pwd():
    password=getpass.getpass("Enter Password: ")
    strength = 0
    remarks =''
    lower_count = upper_count  = num_count = wspace_count = special_count        
    for char in list (password):
        if char in string.ascii_lowercase:
         lower_count += 1
        elif char in string.ascii_uppercase:
         upper_count +=1
        elif char in string.digits:
         num_count += 1
        elif char == '' :
         wspace_count +=1 
        else:
         special_count +=1 

    if lower_count >=1 :
       strength +=1 
    if upper_count >=1 :
       strength +=1
    if  num_count >=1 : 
       strength +=1 
    if wspace_count >=1 :
       strength +=1 
    if special_count >=1 :
       strength +=1 


    if strength == 1:
        remarks = "very Bad password!!! change ASCP  "
    elif  strength == 2 :
        remarks = " Not A good password , change ASCP "
    elif strength == 3 :
       remarks = " Its a weak password, consider changing "
    elif strength == 4 :
       remarks =" it's a hardh password ,but can be better "
    elif strength == 5:
       remarks = " A very stong password "   
    
    print ('your password has: ')
    print(f"{lower_count} lowercase characters")   
    print(f"{upper_count} lowercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace  characters")
    print(f"{special_count} special  characters")
    
    print(f"password strength:{strength}")
    print(f"Hint:{remarks}")
       
def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
       choice=input('Do you want to enter another pwd (y/n):')
    else:
       choice=input('Do yo want to change pwd strength (y/n): ')
    while not valid:
      if choice.lower() == 'y' :
         return True
      elif  choice.lower() == 'n' :
         return False
      else :
         print('Invalid ,try again ')

if __name__ == '__main__':
   print('+++ welcome to PWD cheacker +++')
   ask_pwd = ask_pwd()
   while check_pwd:
      check_pwd()
      ask_pwd = ask_pwd(True)            
