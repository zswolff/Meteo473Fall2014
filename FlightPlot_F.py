class Flight_Plot: 
    """Class that gets the file info and variables, and then plots the variables in four subplots """
    def __init__(self,filename):
        """Function that locates the file for the user"""
        self.filename = filename
    
    def plot_time_series(self):
        """Function where user can enter the start and end time for the variables """
        import UserInput_F as ui
        import GetTime_F as gt
        import GetVariable_F as gv
        import matplotlib
        import matplotlib.pyplot as plt
        import SaveFigures_F as sf
        myinput = ui.User_Input()
        varname = myinput.get_VarName()
        print 'Please enter your start time.'
        start_time = myinput.ask_for_time()
        print 'Please enter your end time.'
        end_time = myinput.ask_for_time()
        mytime = gt.Get_Time(self.filename,start_time,end_time)        
        myvar = gv.Get_Variable(self.filename, varname, start_time, end_time)        
        y = myvar.get_variable_section()
        myunits = myvar.get_units()
        x = mytime.get_time_section()
       
        plt.plot(x,y)
        myfigure = plt.gcf()
        plt.xlabel('Time in HHMMSS')
        plt.ylabel(varname + ' ' + '('+ myunits + ')' )
        plt.title (varname + ' vs. ' + 'Time')
        myfigure = plt.gcf()
        plt.show()
        figure_save = sf.Save_Figures(myfigure,varname)
        figure_save.pick_file_type()
        
        
    def plot_multiple_variables(self):
        """Function""" 
        #Preliminary Multi-panel
        import UserInput_F as ui
        import GetTime_F as gt
        import GetVariable_F as gv
        import matplotlib
        import matplotlib.pyplot as plt      
        import SaveFigures_F as sf
        import numpy as np
        myinput = ui.User_Input()
        print 'Please enter your start time.'
        start_time = myinput.ask_for_time()
        print 'Please enter your end time.'
        end_time = myinput.ask_for_time()
        print 'Please enter each of the four variables you would like to print' 
        vname1 = myinput.get_VarName()
        vname2 = myinput.get_VarName()
        vname3 = myinput.get_VarName()
        vname4 = myinput.get_VarName()
        mytime = gt.Get_Time(self.filename,start_time,end_time)        
        myVar1 = gv.Get_Variable(self.filename,vname1, start_time, end_time)
        myVar2 = gv.Get_Variable(self.filename,vname2, start_time, end_time)
        myVar3 = gv.Get_Variable(self.filename,vname3, start_time, end_time)
        myVar4 = gv.Get_Variable(self.filename,vname4, start_time, end_time)
        Time = mytime.get_time_section()
        Var1 = myVar1.get_variable_section()
        Var2 = myVar2.get_variable_section()
        Var3 = myVar3.get_variable_section()
        Var4 = myVar4.get_variable_section()
        Var1units = myVar1.get_units()
        Var2units = myVar2.get_units()
        Var3units = myVar3.get_units()
        Var4units = myVar4.get_units()
        
        x = np.arange(np.amin(Time),np.amax(Time))
        fig, ax = plt.subplots(2,2)
        fig.subplots_adjust(hspace = 0.5, wspace = 0.5) 
        
        
        ax[0,0].plot(Time, Var1)
        ax[0,0].set_xlabel('Time (HHMMSS)')
        ax[0,0].set_ylabel(vname1 + ' (' + Var1units + ')')
        
        ax[0,1].plot(Time, Var2)
        ax[0,1].set_xlabel('Time (HHMMSS)')
        ax[0,1].set_ylabel(vname2 + ' (' + Var2units + ')')
        
        ax[1,0].plot(Time, Var3)
        ax[1,0].set_xlabel('Time (HHMMSS)')
        ax[1,0].set_ylabel(vname3 + ' (' + Var3units + ')')
        
        ax[1,1].plot(Time, Var4) 
        ax[1,1].set_xlabel('Time (HHMMSS)')
        ax[1,1].set_ylabel(vname4 + ' (' + Var4units + ')')
        mymultiplotfig = plt.gcf()
        figtitle = 'Multipanel plot of ' + vname1 + ', ' + vname2 + ', ' + vname3 + ',and ' +vname4 
        plt.show()
        
        figure_save = sf.Save_Figures(mymultiplotfig, figtitle)
        figure_save.pick_file_type()
        
        
        
        
