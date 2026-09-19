class User_Input: 
    """ A class which takes the user input to be used in any situation where a variable name or time stamp is needed. """
    def ___init__(self): 
        """ An empty init function for the class which does not require any data. """
        data = []

    def get_VarName(self):
        """ A function that gets an input for a variable name from the user. """
        var_name = raw_input('what variable would you like to work with? ')
        return var_name 
   
    def ask_for_time(self): 
        """ A function that gets an input for a time stamp from the user. """
        time = input('please enter time in form of HHMMSS: ')
        return time
    
    
