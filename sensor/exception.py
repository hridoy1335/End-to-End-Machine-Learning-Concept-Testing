# importing dependency
import sys

# get the filename and lineno to find the error to build the custom function
def get_the_error_message(error, error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_no = exe_tb.tb_lineno
    
    error_message = "The Error Occur in file_name is [=> {0} <=] and line_no is [=> {1} <=] or the error_message is [=> {2} <=]".format(
        file_name,line_no,str(error)
    )
    
    return error_message

# Building the sensorexcepton to handle the error
class SensorException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        
        # call the function to get the error details
        self.error_message = get_the_error_message(error=error_message,
                                                   error_detail=error_details)
        
    # returning the string output to visualize clearly 
    def __str__(self):
        return self.error_message