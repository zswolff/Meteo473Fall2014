class Flight_Track:
    """A class which allows the User to plot a map of the flight leg or plots the flight leg in a 3D Plot"""
    def __init__(self,filename):
        """Function that takes the file where the flight data is located."""
        self.filename = filename
    
    def plot_flight_track(self):
        """Function that the user can call to plot the track of the Flight on a map which show major geographical features. """
        import matplotlib
        import matplotlib.cm as cm
        import matplotlib.mlab as mlab
        import matplotlib.pyplot as plt
        from mpl_toolkits.basemap import Basemap
        import GetVariable_F as gv
        import SaveFigures_F as sf
        
        MyLat = gv.Get_Variable(self.filename,'GLAT',0,1)
        MyLon = gv.Get_Variable(self.filename, 'GLON',0,1)
        Lat = MyLat.get_variable_full()
        Lon = MyLon.get_variable_full()
        lat = Lat.flatten()
        lon = Lon.flatten()
        
        m = Basemap(projection='merc', resolution='h',
        llcrnrlon=-78, llcrnrlat=42,
        urcrnrlon=-74, urcrnrlat=44, )        
        m.drawcoastlines()
        m.drawstates()
        m.drawcounties()
        m.drawcountries()
        m.fillcontinents(color='green',lake_color='SteelBlue')
        
        x,y = m(lon,lat)
        m.plot(x, y,'b', markersize = 5)
        
        #Creates markers for major cities in the vicinity of our Flight path
        lon1 = [-76.145398,-77.611546,-76.502185]
        lat1 = [ 43.045525,43.153811,42.442701]

        a,b =m(lon1,lat1)

        m.plot(a, b, 'ro', markersize = 4)

        labels = [' Syracuse', ' Rochester', 'Ithaca']
        for label, xpt, ypt in zip(labels, a, b):
            plt.text(xpt-10000, ypt+6000, label)
        

        m.drawmapboundary(fill_color='blue')
        plt.title('Flight Track Path')
        mymapfigure = plt.gcf()
        plt.show()
        MapSave = sf.Save_Figures(mymapfigure, 'Flight Track Path')
        MapSave.pick_file_type()
    
    def plot_3D_flight_track(self):
        """This function allows the viewer to look at the track of the flight path, not
        only in dimensions of latitude and longitude, but also with the altitude of the
        flight. This is plotted in a three-dimensional graph."""
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import GetVariable_F as gv
        import SaveFigures_F as sf
        MyAlt = gv.Get_Variable(self.filename,'GALT',0,1)
        MyLon = gv.Get_Variable(self.filename,'GLON',0,1)
        MyLat = gv.Get_Variable(self.filename,'GLAT',0,1)
        alt =  MyAlt.get_variable_full().flatten()
        lon =  MyLon.get_variable_full().flatten()
        lat =  MyLat.get_variable_full().flatten()
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(lon, lat, alt, '-b')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Altitude (m)')
        plt.title('3D Flight Track Path')
        my3dfig = plt.gcf()
        plt.show()
        Save3D = sf.Save_Figures(my3dfig, '3D Flight Track Path')
        Save3D.pick_file_type()
    
