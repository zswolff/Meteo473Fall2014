import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import GetVariable as Gv
import Save as sf

class Radar_and_Lidar:
    """This class takes the lidar and radar variables and plots graphs"""
    
    def __init__(self, filename, save_type):
        """ This function gets the filename and saving method specified by the driver """
        self.filename = filename
        self.ftype = save_type
    
    def WCR_Plot(self,z_var,graph_title,z_axis): 
        """This function takes the WCR varable and plots it in a Time-Height graph"""
        T = Gv.Get_Variable(self.filename,'time','N/a', 'N/a')
        A = Gv.Get_Variable(self.filename, 'altrange', 'N/a', 'N/a')
        R = Gv.Get_Variable(self.filename, z_var,'N/a', 'N/a')
        time = T.get_variable_full()
        ddays = (time%86400.)/(86400.)
        dhours = (ddays - np.floor(min(ddays)))*24                                
        
        x = dhours
        y = A.get_variable_full()
        z = R.get_variable_full()
      

        plt.pcolormesh(x,y,z.T,cmap = 'gist_ncar')
        plt.title(graph_title)
        plt.axis([x.min(),x.max(),y.min(),y.max()])
        plt.xlabel('Time (decimal hours)')
        plt.ylabel('Altitude (m)')
        cbar = plt.colorbar()
        cbar.set_label(z_axis)
        Radar_plot = plt.gcf()
        plt.show()
        figure_save = sf.Save_Figures(Radar_plot, graph_title, self.ftype)
        figure_save.pick_file_type()   
    
    def WCL_Plot(self):
        """ This function makes a subplot display showing the lidar plots of CopolHiPower, CrossHiPower, CrossHiPower divided by CopolHiPower 
        and the difference between CopolHiPower and CrossHiPower"""
        T = Gv.Get_Variable(self.filename,'Time','N/a', 'N/a')
        A =  Gv.Get_Variable(self.filename,'Range','N/a', 'N/a')
        Cop = Gv.Get_Variable(self.filename,'CopolHiPower','N/a', 'N/a')
        Cro = Gv.Get_Variable(self.filename,'CrossHiPower','N/a', 'N/a')
        
        time = T.get_variable_full()
        Alt = A.get_variable_full()
        CoHigh = Cop.get_variable_full()
        CrHigh = Cro.get_variable_full()          
        ddays = (time%86400.)/(86400.)
        dhours = (ddays - np.floor(min(ddays)))*24
           
        x = dhours
        y = Alt
        fig, ax = plt.subplots(2,2,figsize= (20,15))
        fig.subplots_adjust(hspace = 0.5)

        z1 = np.flipud(10*np.log10(CoHigh))
        z1[z1 == -np.inf]= np.nan
        z1_min= np.nanmin(z1)
        z1_max= np.nanmax(z1)

        z2 = np.flipud(10*np.log10(CrHigh))
        z2[z2 == -np.inf]= np.nan
        z2_min= np.nanmin(z2)
        z2_max= np.nanmax(z2)

        z3 = z2/(1000000*z1)
        z3[z3 == -np.inf]= np.nan
        z3_min= np.nanmin(z3)
        z3_max= np.nanmax(z3)

        z4 = z1-z2
        z4[z4 == -np.inf]= np.nan
        z4_min= np.nanmin(z4)
        z4_max= np.nanmax(z4)


        cs1= ax[0,0].pcolormesh(x,y,z1, cmap = 'gist_ncar', vmin = z1_min, vmax = z1_max)
        ax[0,0].set_title('Time-Height Plot of WCL Copol High Reflectivity', fontsize= 12)
        ax[0,0].set_xlabel('Time', fontsize= 12)
        ax[0,0].set_ylabel('Altitude (m)',fontsize= 12)
        ax[0,0].set_xlim(np.amin(x),np.amax(x))
        ax[0,0].set_ylim(0,np.amax(y))
        cbar1 = plt.colorbar(cs1,ax=ax[0,0])
        cbar1.set_label('Power (mW)')


        cs2= ax[0,1].pcolormesh(x,y,z2, cmap = 'gist_ncar', vmin = z2_min, vmax = z2_max)
        ax[0,1].set_title('Time-Height Plot of WCL Cross High Reflectivity', fontsize= 12)
        ax[0,1].set_xlabel('Time',fontsize= 12)
        ax[0,1].set_ylabel('Altitude (m)',fontsize= 12)
        ax[0,1].set_xlim(np.amin(x),np.amax(x))
        ax[0,1].set_ylim(0,np.amax(y))
        cbar2 = plt.colorbar(cs2,ax=ax[0,1])
        cbar2.set_label('Power (mW)')


        cs3= ax[1,0].pcolormesh(x,y,z3, cmap = 'gist_ncar', vmin = z3_min, vmax = z3_max)
        ax[1,0].set_title('Time-Height Plot of High Reflectivity Depolarization', fontsize= 12)
        ax[1,0].set_xlabel('Time', fontsize= 12)
        ax[1,0].set_ylabel('Altitude (m)',fontsize= 12)
        ax[1,0].set_xlim(np.amin(x),np.amax(x))
        ax[1,0].set_ylim(0,np.amax(y))
        cbar3 = plt.colorbar(cs3,ax=ax[1,0])



        cs4= ax[1,1].pcolormesh(x,y,z4, cmap = 'gist_ncar', vmin = z4_min, vmax = z4_max)
        ax[1,1].set_title('Time-Height Plot of Copol and Cross Reflectivity Difference', fontsize= 12)
        ax[1,1].set_xlabel('Time', fontsize= 12)
        ax[1,1].set_ylabel('Altitude (m)',fontsize= 12)
        ax[1,1].set_xlim(np.amin(x),np.amax(x))
        ax[1,1].set_ylim(0,np.amax(y))
        cbar4 = plt.colorbar(cs4,ax=ax[1,1])
        cbar4.set_label('Power (mW)')
        
        Lidar_plot = plt.gcf()
        plt.show()
        figure_save = sf.Save_Figures(Lidar_plot, 'Time-Height WCL plots', self.ftype)
        figure_save.pick_file_type()  
        
    def FileTypePlot(self):
        """Function that recognizes whether or not the filename is that of WCL or WCR""" 
        if "WCL" in self.filename:
            self.WCL_Plot()   
        if "WCR" in self.filename:
            self.WCR_Plot('reflectivity','Time-Height WCR Reflectivity','Reflectivity (dBZ)')
            self.WCR_Plot('velocity', 'Time-Height WCR Velocity', 'Velocity (m/s)')
        
