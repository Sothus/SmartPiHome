import pigpio

class RGB_LED:

    def __init__(self, *args, **kwargs):
        if 'pi' in kwargs:
            self._pi = kwargs['pi']
        elif ('ip' in kwargs) and ('port' in kwargs):
            self._pi = pigpio.pi(kwargs['ip'], kwargs['port'])
        else:
            raise NameError("Missing arguments for pigpio initialization")

        if not self._pi.connected:
            raise ConnectionRefusedError("Can't connect to Raspberry")

        self._on = False
        self._pins  = {
            "red":      args[0],
            "green":    args[1],
            "blue":     args[2],
        }
        self._colors = {
            "red":      0,
            "green":    0,
            "blue":     0,
        }

        for pin in self._pins:
            self._pi.set_mode(self._pins[pin], pigpio.OUTPUT)

        #Prevents LED from flashing
        self._pi.set_PWM_frequency(8000)


    def on(self):
        for pin in self._pins:
            self._pi.set_PWM_dutycycle(self._pins[pin], self._colors[pin])
        self._on = True


    def off(self):
        for pin in self._pins:
            self._pi.set_PWM_dutycycle(self._pins[pin], 0)
        self._on = False


    def set_color(self, **kwargs):
        if 'red' in kwargs:
            self._colors['red'] = kwargs['red']
        if 'green' in kwargs:
            self._colors['green'] = kwargs['green']
        if 'blue' in kwargs:
            self._colors['blue'] = kwargs['blue']

        #Refreshing LEDs
        if self._on == True:
            self.on()
