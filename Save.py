import matplotlib 
import matplotlib.pyplot as plt 
class Save_Figures: 
    """This class gives the user the choice of saving their plots to either a pdf, png, or 
    postscript file."""
    def __init__ (self,figure,title,f_type):
        
        self.figure = figure
        self.title = title
        self.f_type = f_type
    def save_figure(self,file_type):
        """ Function that allows the user to either save plots for all of the available file types, or just for one specific type. """        
        if file_type == 'ALL':
           self.save_figure('pdf')
           self.save_figure('ps')
           self.save_figure('png')
        else:
       
           f = open(self.title + '.' + file_type, 'w')
           self.figure.savefig(f, dpi = 400)
           f.close()
    def pick_file_type(self):
        """Function that asks the user to input what type of file format the plot should save as."""
        file_type = self.f_type
        self.save_figure(file_type)
        
