print('welcome to book my show')
name=(input('enter your name:-'))
seats=int(input('enter no of seats you want to book'))
category= int (input('please select 1...> diamond class \n 2...>glod class,\n,3..>sliver calss.'))
if category ==1:
    amount=seats*200                        
if category ==2:
    amount=seats*150
if category ==3:
    amount=seats*100
print(f'hi{name}you have  booked{seats}seats and totalamount is{amount}')                            
                        

    
 










 

