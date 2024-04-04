class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        arr = []
        Kelvin = 0.0
        Fahrenheit = 0.0
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        arr.append(Kelvin)
        arr.append(Fahrenheit)
        return arr