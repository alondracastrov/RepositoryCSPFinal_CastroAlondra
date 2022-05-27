# RepositoryCSPFinal_CastroAlondra
Random Password Generator and Calculator using python

**Calculator:**
-This is a GUI calculator written in python which calculates expressions based on what buttons the user presses. We have a calculation string which starts empty. This program consists of 3 functions. 
-The first is called  addToCalculation with a parameter called symbol. In this function,  calculation is a global  variable and will always be type casted into a string and will be then added to the calculation string.  We also delete the content of the text result field and insert the calculation string.
- The second function is called  evaluateCalculation which will call the eval  function and do the necessary tkinter operations. The string from the calculation will be evaluated using the eval function. In this function, we try by evaluating the calculation  and turning it into a string and saving it as a result. We ill also catch any exceptions (errors) by using except. 
- The third function is called ClearField. Here we reset the calculation global variable and delete the text result.
-I built a basic GUI to have a text field that follows the desired operations. I did this starting from   the starting point of ‘root= tk.Tk() and the end point root.mainloop(),  we  create the object and run the  main loop. Between these will be all  the components that make up the GUI  such  as the  geometry   of the app, buttons,etc.


**Why I chose to do this project:** I chose to make the calculator as one of my project because it seemeed like a nice challenge and would 
give me an interesting end product I could show my friends.
 
 **Password Generator**
 -This is a random password generator which creates passcodes  randomly based on two inputs from the user.
-First we import random and then we specify the characters that will be used to create the random password. This function contains a main loop and inside that loop the program asks the  user to input the desired length of the password and stores it in a variable called password_length. It also asks the user to input how many passwords they would like and stores it in a variable called passwords_generated.
-We then give the loop a range of how many  times it's gonna run using for x  in range. In this case it will run as many times as the user wants to generate a password. For example, if the user types that they want three  passwords it will run three times.
-For the part that creates the password we use another for loop with a range of how many characters the user wants in their password (from 0 until password length has been met). Basically, we will run this  loop the number of times the user wants their length to be. Each time this loop runs, one character will be added to the password until the final  length. Every time this  loop runs it will grab the password character by equaling the variable password_character to a random choice that  selects a single character from the characters string. Finally, each character will be added to the final password variable until it forms the  complete password.

