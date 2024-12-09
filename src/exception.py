import sys
from src.logger import logging
#import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


# # Test the CustomException class
# if __name__ == "__main__":
#     try:
#         # Simulate an error (division by zero)
#         x = 1 / 0
#     except Exception as e:
#         # Raise CustomException and log the error
#         custom_error = CustomException(str(e), sys)
#         logging.error(custom_error)
#         print(custom_error)        