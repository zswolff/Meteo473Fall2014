"""This program takes the flight track and our previous flight plot  and creates a one-dimensional 
time series plot as well as a multivariate plot. The program also plots the flight track in two and
three dimensions for the viewer's benefits."""
import FlightPlot_F as fp
import FlightTrack_F as ft
Valid_File = False 
while Valid_File == False: 
    MyDataFile = raw_input('Please write full path to the file: ')
    
    try:
        MyPlot = fp.Flight_Plot(MyDataFile)
        MyPlot.plot_time_series()
        MyPlot.plot_multiple_variables()

        MyMap = ft.Flight_Track(MyDataFile)
        MyMap.plot_flight_track()
        MyMap.plot_3D_flight_track()
        Valid_File = True
   
    except:
        print 'Not a vaild file path. Please try again.'
        Valid_File = False  
    
print "Thank you! Goodbye!"

