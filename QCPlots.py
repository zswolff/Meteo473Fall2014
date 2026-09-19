import numpy as np
from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import RadarLidar1 as Rl
import GetVariable as Gv
import Save as Sf


class QC_Plots: 
    """This class creates plots for both QC variables, saves them to a driver-selected file type, and checks to make sure the radar and lidar variables are coming
    from the appropriate data set."""
    
    def __init__(self,filename,save_type):
        """This function allows for other functions to be used as object classes."""
        self.filename = filename
        self.ftype = save_type
        
    def WCR_Mask(self):
        """This function plots the radar QC variable, WCRmask, as a time-height chart."""
        Mask_plot = Rl.Radar_and_Lidar(self.filename, self.ftype)
        Mask_plot.WCR_Plot('wcrmask','Time-Height Plot of WCR Mask','WCR Mask')
    def WCL_QC(self,Qc_var,graph_title,qc_var_axis):
        """This function plots the lidar QC variable, Prof_qc_flag, as a time-series chart."""
        T = Gv.Get_Variable(self.filename,'Time','N/a', 'N/a')
        Q = Gv.Get_Variable(self.filename, Qc_var,'N/a', 'N/a')
        time = T.get_variable_full()
        ddays = (time%86400.)/(86400.)
        dhours = (ddays - np.floor(min(ddays)))*24 
              
        x = dhours
        y = Q.get_variable_full()

        plt.plot(x,y)
        plt.xlabel('Time (decimal hours)')
        plt.ylabel(Qc_var)
        plt.title (graph_title)
        Qc_plot = plt.gcf()
        plt.show()
        figure_save = Sf.Save_Figures(Qc_plot, graph_title, self.ftype)
        figure_save.pick_file_type()
   
    
    def QC_File_Type(self):
        """This function makes sure that the WCRmask data is coming from the radar data set, and that the lidar variables are coming out 
        of the lidar data set."""
        if "WCL" in self.filename:
            self.WCL_QC('Prof_qc_flag', 'Time vs. QC Flag', 'QC Flag')  
            self.WCL_QC('Pitch', 'Time vs. Pitch', 'Pitch') 
            self.WCL_QC('Roll', 'Time vs. Roll', 'Roll') 
        if "WCR" in self.filename:
            self.WCR_Mask()
       
        
            

