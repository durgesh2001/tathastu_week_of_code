 len=int(input("enter the range"))
 for i in range(0, len): 
      
        j = len -1 - i 
        for k in range(0, len): 
          
            if (k == i or k == j): 
                print("*",  end = "") 
            else: 
                print(end = " ") 
          
        print(" ")  
