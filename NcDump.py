class NcDump: 
    """A class which upon being given a file name with full path can dump metadata to a csv file as well as printing out a selected variable to txt file.""" 
    def __init__(self,filename):
        """Function which fills the class with the flight data we wish to use."""   
        self.filename=filename
    
    def open_file(self):
        """Takes file name and opens file associated with said file."""
        from netCDF4 import Dataset
        
        myfile = self.filename
        ncfile = Dataset(myfile, 'r')
        return ncfile 
    
    def nc_dump(self):
        """"Takes the file, opens it, and dumps selected meta data into a csv file. """
        import csv
        import numpy as np
        
        Mydata = self.open_file()
        with open('Flight_Info.csv','w') as f:
            a = csv.writer(f)
            a.writerow(('variable name','longname', 'units', 'dimensions', 'shape')) 
    
            for key, value in Mydata.variables.iteritems():
                if hasattr(value, 'long_name') == True:
                    name = value.long_name                 
                else: 
                    name = ' '      
                
                if hasattr(value, 'units') == True:
                    units = value.units
                    
                if hasattr(value, 'dimensions') == True: 
                    dimensions = value.dimensions 
                
                shape = np.shape(value)
                
                a.writerow((key,name,units,dimensions,shape)) 
        
        f.close()
    
    def print_variable(self):
        """Asks user for a varaible to print and prints variable to file, allows user to repeat process and print additional variables . """        
        Mydata = self.open_file()
        print 'What variable would you like to print?'
        run_again = True
       
        while run_again == True:         
            var_name = raw_input('Please write the short-form name of the element you wish to print: ')
            try: 
                myval = Mydata.variables[var_name][:].flatten()
                i=0
                x= myval[i]
                f = open(var_name+'.txt', "w")
                for x in myval:
                    print >> f, x
                    i=i+1
                    
                print_another = raw_input('Would you like to run again? Please enter y to continue or any other key to end: ')                
                if print_another == 'y':
                    run_again = True 
                else:
                    run_again = False 
                    print 'Goodbye!'
    
            except: 
                print 'Invalid variable name. Please check the spelling and capitalization, and try again.' 
                run_again = True 
                        
