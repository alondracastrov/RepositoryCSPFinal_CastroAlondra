# RepositoryCSPFinal_CastroAlondra
Random Password Generator and Calculator using python

**Calculator:**
-This is a GUI calculator written in python which calculates expressions based on what buttons the user presses.
-We have a calculation string which starts empty. This program consists of 3 functions. The first is called  addToCalculation with a parameter called symbol. In this function,  calculation is a global  variable and will always be type casted into a string and will be then added to the calculation string.  We also delete the content of the text result field and insert the calculation string.
- The second function is called  evaluateCalculation which will call the eval  function and do the necessary tkinter operations. The string from the calculation will be evaluated using the eval function. In this function, we try by evaluating the calculation  and turning it into a string and saving it as a result. We ill also catch any exceptions (errors) by using except. 
- The third function is called ClearField. Here we reset the calculation global variable and delete the text result.
-I built a basic GUI to have a text field that follows the desired operations. I did this starting from   the starting point of ‘root= tk.Tk() and the end point root.mainloop(),  we  create the object and run the  main loop. Between these will be all  the components that make up the GUI  such  as the  geometry   of the app, buttons,etc.


**Why I chose to do this project:** I chose to make the calculator as one of my project because it seemeed like a nice challenge and would 
give me an interesting end product I could show my friends.
 
