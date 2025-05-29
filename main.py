import sys
from sensor.exception import SensorException

def custom_error():
    try:
        1/0
    except Exception as e:
        raise SensorException(e,sys)
    
if __name__ == "__main__":
    try:
        custom_error()
    except Exception as e:
        print(e)