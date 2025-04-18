

class SmartDevice:
    
    '''This parent class allows us to gather name of device and whether it is on or off,
    we can change whether it is or not, printing instance will display this.'''
    
    
    def __init__(self, name, status = False):
        
        '''Initializes for all SmartDevices its name and its status'''

        
        self.name = name
        self.status = status

    
    def turn_on(self):
        
        '''This turns on the SmartDevice by making status True'''
        
        self.status = True



    
    def turn_off(self):
        
        '''This turns off the SmartDevice by making status True'''
        
        self.status = False

    
    def __str__(self):
        
        '''This returns the name of the device and its status if instance is asked to be printed.'''
        
        if self.status == True:
            return(f'{self.name}: ON')
        else:
            return(f'{self.name}: OFF')
    


class Light(SmartDevice): #A Light is a SmartDevice
    
    '''This class is for lights, which is a smart device and takes its brightness'''
    
    def __init__(self, name, brightness = 100):
        
        '''Initializes SmartDevice name and adds brightness attribute'''

        super().__init__(name)
        if brightness > 100:
            self.brightness = 100 
        else:
            self.brightness = brightness
    
    
    def adjust_brightness(self, level):
        
        '''Sets brightness level if given value is between range 0-100'''
        
        if int(level)<100 and int(level)>0:
            self.brightness = level

    
    def __str__(self):
      
        '''This returns the name of the device and its status if instance is asked to be printed 
        alongside its brightness.'''
      
        return(f'{SmartDevice.__str__(self)}, Brightness: {self.brightness}')
    


class Thermostat(SmartDevice): #A Thermostat is a SmartDevice

    '''This class is for Thermostats and allows you to change temperature to a 
    reasonable setting'''

    def __init__(self, name, temperature = 65):
        
        '''Initializes Thermostat Smart Device name and adds temperature attribute'''
       
        super().__init__(name)
        self.temperature = temperature

    
    def _check_temperature_limits(self, temperature):
        
        '''Returns True boolean if temp in range, otherwise returns False boolean'''
        
        if (float(temperature) <= 80) and (float(temperature) >= 55):
            return(True)
        else:
            return(False)
    
    
    def adjust_temperature(self, temperature):
        
        '''Allows temperature attribute to be changed using private method checking if its in range'''

        if ((Thermostat._check_temperature_limits(self, temperature)) == True):
            self.temperature = temperature

    
    def __str__(self):
        
        '''This returns the name of the device and its status if instance is asked to be printed 
        alongside its temperature.'''
        
        return((f'{SmartDevice.__str__(self)}, Temperature: {self.temperature}'))
    


class Speaker(SmartDevice): #A speaker is a SmartDevice
    
    
    '''This is for the Speaker. We are able to increase and decrease its volume'''
    
    
    def __init__(self, name, volume = 3):
        
        '''Initializes SmartDevice name and adds volume attribute'''
        
        super().__init__(name)
        if (volume >= 1) and (volume <= 10):
            self.volume = volume
        else:
            self.volume = 3


    def increase_volume(self):
        
        '''This function raises volume by one if volume is 10 or less'''
        
        if ((self.volume+1 >= 1) and (self.volume+1 <= 10)):
            self.volume += 1


   
    def decrease_volume(self):
        
        '''This function lowers volume by one if volume is below 1'''
        
        if (self.volume-1 >= 1):
            self.volume -= 1


    def __str__(self):
        
        '''This returns the name of the device and its status if instance is asked to be printed 
        alongside its volume.'''
        
        return((f'{SmartDevice.__str__(self)}, Volume: {self.volume}'))



class SmartHome: #SmartHome HAS a smart device, but is not one
    
    
    '''This gets all the smart devices of the Smart House, we can add all smart devices to list'''
    
    def __init__(self):
        self.devices = []


    def __add__(self, other): #other is what we add to it; (x+y) y is other. Self is x.

        '''This device adds instance of a SmartDevice using + function'''
        
        self.devices.append(other)
        return(self) #now when self.devices is brought up, brings list
        

    def turn_off_all(self):

        '''This method turns off all devices by going through all and setting status to false'''

        for device in self.devices:
            SmartDevice.turn_off(device)


    def __str__(self):
        
        '''This method goes through every device in list and returns its name and status'''
        
        device_list = []
        for device in self.devices:
            device_list.append(SmartDevice.__str__(device))
        return(f"{', '.join(device_list)}")