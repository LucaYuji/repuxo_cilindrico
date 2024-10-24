from math import pi , sqrt

# Functions to calculate the surface area of ​​each shape and function to calculate the volume

class BlankCalculation:
    def __init__(self, thickness= 1):
        self.thickness = thickness
    
    #  ||   ||  ->  shape

    def cylinder(self, height, medium_diameter= 0., outer_diameter= 0., inner_diameter= 0.):
        if outer_diameter != 0.:
            medium_diameter = outer_diameter - self.thickness
            surface_area = pi * medium_diameter * height
        elif inner_diameter != 0.:
            medium_diameter = inner_diameter + self.thickness
            surface_area = pi * medium_diameter * height
        elif medium_diameter != 0.:         
            surface_area = pi * medium_diameter * height
        return surface_area

    #  --    --  ->  shape

    def washer(self, outer_diameter, inner_diameter):
        surface_area = (pi * ((outer_diameter**2) - (inner_diameter**2))) / 4
        return surface_area
    
    # ""|    |""  ->  shape

    def funnel(self, outer_diameter= 0., inner_diameter= 0., smaller_radius= 0., larger_radius= 0., medium_radius= 0.):
        if outer_diameter != 0.:
            if smaller_radius != 0.:
                medium_radius = smaller_radius + (self.thickness / 2)
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
            elif larger_radius != 0.:
                medium_radius = larger_radius - (self.thickness / 2)
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
            elif medium_radius != 0.:
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
        elif inner_diameter != 0.:
            if smaller_radius != 0.:
                outer_diameter = inner_diameter + (2 * self.thickness) + (2 * smaller_radius)
                medium_radius = smaller_radius + (self.thickness / 2)
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
            elif larger_radius != 0.:
                outer_diameter = inner_diameter + (2 * larger_radius)
                medium_radius = larger_radius - (self.thickness / 2)
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
            elif medium_radius != 0.:
                outer_diameter = inner_diameter + self.thickness + (2 * medium_radius)
                surface_area = (((pi**2) * medium_radius * outer_diameter) / 2) - 2 * pi * (medium_radius**2)
        return surface_area

    # --------  ->  shape 

    def coin(self, diameter):
        surface_area = (pi * (diameter**2)) / 4
        return surface_area
    
    # |_     _|  ->  shape

    def fender(self, outer_diameter= 0., inner_diameter= 0., smaller_radius= 0., larger_radius= 0., medium_radius= 0.):
        if outer_diameter != 0.:
            if smaller_radius != 0.:
                inner_diameter = outer_diameter - ((2 * self.thickness) + (2 * smaller_radius)) 
                medium_radius = smaller_radius + (self.thickness / 2)
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
            elif larger_radius != 0.:
                inner_diameter = outer_diameter - (2 * larger_radius)
                medium_radius = larger_radius - (self.thickness / 2)
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
            elif medium_radius != 0.:
                inner_diameter = outer_diameter - self.thickness - (2 * medium_radius)
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
        elif inner_diameter != 0.:
            if smaller_radius != 0.:
                medium_radius = smaller_radius + (self.thickness / 2)
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
            elif larger_radius != 0.:
                medium_radius = larger_radius - (self.thickness / 2)
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
            elif medium_radius != 0.:
                surface_area = (2 * pi * (medium_radius**2)) + (((pi**2) * medium_radius * inner_diameter) / 2)
        return surface_area
    
    # |__|  ->  shape

    def concave(self, smaller_radius= 0., larger_radius= 0.):
        if smaller_radius != 0.:
            medium_radius = smaller_radius + (self.thickness / 2)
            surface_area = 2 * pi * (medium_radius**2)
        elif larger_radius != 0.:
            medium_radius = larger_radius - (self.thickness / 2)
            surface_area = 2 * pi * (medium_radius**2)
        return surface_area    

    # Volume calculation

    def blank(self, surface_area= 0., cup_volume= 0.):
        if surface_area != 0.:
            blank_diameter = sqrt((4 * surface_area) / pi)
        elif cup_volume != 0.:
            blank_diameter = sqrt((4 * cup_volume) / (pi * self.thickness))
        return blank_diameter