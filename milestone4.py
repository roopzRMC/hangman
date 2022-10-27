# %%
import math

class Cylinder:

    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume=None


    def get_surface_area(self):
        self.surface_area =  round((2*math.pi*self.radius*self.height + 2*math.pi*self.radius**2), 2)
        return self.surface_area 
    
    def get_volume(self):
        self.volume =  round((math.pi*self.radius**2*self.height), 2)
        return self.volume
    


# %%
myCyl = Cylinder(20,5)
# %%
myCyl.get_surface_area()
# %%
myCyl.get_volume()
# %%
myCyl.surface_area
# %%
myCyl.volume
# %%
