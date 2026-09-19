"""A program which takes class NcDump and allows the user to input the file path  """
import NcDump as nd
Valid_File = False 
while Valid_File == False: 
    MyDataFile = raw_input('Please write full path to the file: ')
    
    try:
        FileDump = nd.NcDump (MyDataFile) 
        FileDump.nc_dump() 
        FileDump.print_variable()
        Valid_File = True
   
    except:
        print 'Not a vaild file path. Please try again.'
        Valid_File = False  
    
    


