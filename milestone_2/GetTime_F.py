class Get_Time: 
    """ This class takes in the user inputed start and end times and finds the time legs and corrects for the specific variables inputed """
    def __init__(self,filename,time1,time2): 
        """ Function that pulls the start to end times of the entire flight path for the user. """
        self.filename = filename
        self.time1 = time1
        self.time2 = time2
    def get_time(self):
        """Function that retrieves all of the times for every variable in the flight 
        leg for the user to choose from."""
        import GetVariable_F as gv
        Variable = gv.Get_Variable(self.filename,'TIME',self.time1,self.time2)
        time = Variable.get_variable_full()
        return time
    def get_starti(self):
        """ """
        start_time = self.time1
        time_spot = 1
        starti = self.get_timei(time_spot)
        return starti
    def get_endi(self):
        """ """
        end_time = self.time1
        time_spot = 2
        endi = self.get_timei(time_spot)
        return endi
    def get_timei(self,time_spot): 
        """Function where the times inputted by the user are run through a loop, where it checks to see if those
        times are within the start and stop time boundaries of the flight leg."""
        import GetVariable_F as gv
        Variable = gv.Get_Variable(self.filename,'TIME',self.time1,self.time2)
        time = Variable.get_variable_full()
        if time_spot ==1:
            mytime = self.time1
        elif time_spot == 2:
            mytime = self.time2
        else:
            print "invalid function use."
        i = 0
        numel = len(time)
        while i < numel:
            T = time[i]
            if T == mytime: 
                timeindex = i 
                break 
            else: 
                i = i+1                 
        return timeindex

    def get_time_section(self):
        """Function that returns the actual start and end times that the user entered, since
        there are 25 measurements taken per second."""
        import numpy as np 
        time = self.get_time()
        starti = self.get_starti()
        endi = self.get_endi()
        time_sect = time[starti:endi]
        time_correct = np.linspace(time[starti]*25,(time[endi]*25)+1, num= 25*len(time_sect))/25
        return time_correct
        
     
        
