from qcodes.instrument_drivers.rohde_schwarz.SGS100A import RohdeSchwarzSGS100A
from abc import ABC, abstractmethod

class sgs100A():

    def __init__( self, address:str ):
        self.sgs = RohdeSchwarzSGS100A('sgs', address=address)
    
    @abstractmethod
    def CW_output( self, frequency_Hz:float=6e9, power_dBm:float=-20):
        self.sgs.frequency(frequency_Hz)
        self.sgs.power(power_dBm)
        self.sgs.on()
    
    @abstractmethod
    def CW_shutdown( self ):
        self.sgs.off()
