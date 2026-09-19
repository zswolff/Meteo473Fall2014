class Get_Variable:
    """This class takes in variables inter"""
    
    def __init__ (self,filename,VarName,time1,time2): 
        self.filename = filename
        self.variable = VarName
        self.time1 = time1
        self.time2 = time2
    
    def get_variable_full(self): 
        """ Function where when the user enters a variable, it checks to see if such variable exists, otherwise it tells the user to try again."""   
        from netCDF4 import Dataset
        myfile = self.filename
        ncfile = Dataset(myfile, 'r')
        myvarname = self.variable
        try:
            myvar = ncfile.variables[myvarname][:]
            return myvar
        except:
            print "Invalid Variable please try again." 
            
    def get_variable_section (self):
        """ """
        import GetTime_F as gt
        time = gt.Get_Time(self.filename, self.time1, self.time2)
        starti = time.get_starti()
        endi = time.get_endi()
        variable = self.get_variable_full()
        myvariable = variable[starti:endi]
        myvarsection = myvariable.flatten()
        return myvarsection 
    
    def get_units (self):
        """ Function where the units for the variables entered by the user are retrieved """
        from netCDF4 import Dataset
        myfile = self.filename
        ncfile = Dataset(myfile, 'r')
          
        for key, value in ncfile.variables.iteritems():
            if key == self.variable:                   
                if hasattr(value, 'units') == True:
                    units = value.units
                return units 
                    
                
                
               
    
    
                   
   


    
    
        
