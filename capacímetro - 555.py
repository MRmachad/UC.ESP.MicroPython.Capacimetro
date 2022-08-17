from machine import Pin
import time

P_Carg = Pin(23, Pin.IN)
P_Req_Carg = Pin(23, Pin.OUT)

class freq_req():

    start = time.ticks_us()
    stop = time.ticks_us() 
    RA = 1000
    RB = 10000
    capacitor = 0
    f  = 0
    T = 0
    
    def time_RISING(self, p):
        aux = time.ticks_us()
        self.start = self.stop
        self.stop = aux
        self.T = time.ticks_diff(self.stop, self.start) * pow(10,-6)N

        self.f = 1/(self.T)
        
        
        self.capacitor = pow(10, 6) * (1.44/((self.RA + 2*self.RB)*self.f))
        obj.print_Line()
        
        
        
    def print_Line(self):
        print("\x1b[2J\x1b[1;1H")
        print("\nCAPACITOR: ", self.capacitor, " uF |","Frequencia: ", self.f," hz |","Periodo: ", self.T," s|","ERRO 1: ", (self.capacitor - 10), "ERROR 2", (self.capacitor - 20),"\n")
    
obj = freq_req()
P_Carg.irq(handler =obj.time_RISING , trigger = Pin.IRQ_RISING)
while(1):
    pass
    
   
    
   
    
    
    