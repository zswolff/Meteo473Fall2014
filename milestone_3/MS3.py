"""This program imports previously made plots, using data from hard-coded data files, and saves them as separate file types."""
import RadarLidar1 as Rl
import QCPlots as Qc


WCRfile = '/risk/s0/g3y/WCR/WCR.OWLES13.20131210.164520_172355.up-down.nc'
WCLfile = '/risk/s0/g3y/WCL/WCL4.DOWN.OWLES13.20131210.164312-164960.nc'
Save_type = 'ALL'


Radar_plots = Rl.Radar_and_Lidar(WCRfile,Save_type)
Radar_plots.FileTypePlot() #Plots Radar Reflectivity and Velocity.

Lidar_plots = Rl.Radar_and_Lidar(WCLfile,Save_type)
Lidar_plots.FileTypePlot() #Plots Lidar Reflectivity.

QC_Radar = Qc.QC_Plots(WCRfile,Save_type)
QC_Radar.QC_File_Type() #Plots Radar WCR mask QC variable.

QC_Lidar = Qc.QC_Plots(WCLfile,Save_type)
QC_Lidar.QC_File_Type() #Plots Lidar QC flag and pitch and roll.

