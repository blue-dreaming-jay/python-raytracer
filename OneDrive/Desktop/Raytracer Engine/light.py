from colour import Colour
from vector import Vector

def incidence(angle, max_angle):
    if angle>max_angle:
        return 0
    if angle==0:
        return 1
    rel_strength=((max_angle-angle)/max_angle)
    return rel_strength

class Light(object):
    def __init__(self, id, position, colour, strength, max_angle, func=0):
          self.id=id
          self.position=position
          self.colour=colour
          self.strength=strength
          self.max_angle=max_angle
          self.func=func
    
    def lambert_light(self, obj, colour, point, light_val):
        normal_vector=point.subtract_vectors(obj.centre)
        incidence_vector=point.subtract_vectors(self.position)

        ratio=max(normal_vector.dot_prod(incidence_vector)/(normal_vector.magnitude()*incidence_vector.magnitude()), 0)

        final_col=colour.addcolour(light_val).scalecolour(ratio)

        return final_col

    def illuminate(self, obj):
        colour=obj.colour
        r_factor=self.colour.r/255
        g_factor=self.colour.g/255
        b_factor=self.colour.b/255

        return Colour(min(255, round(colour.r*(1+r_factor))), min(255, round(colour.g*(1+g_factor))), min(255, round(colour.b*(1+b_factor))))
    
class PointLight(Light):
     def relativeStrength(self, angle, distance):
        if self.func == -1:
            return self.colour.scaleRGB(incidence(angle, self.max_angle) * self.strength)
        if self.func == 0:
            return self.colour.scaleRGB(incidence(angle, self.max_angle) * self.strength / distance)

class GlobalLight(Light):
    def relativestrength(self, angle, distance):
        return self.colour.scaleRGB(incidence(angle, self.max_angle) * self.strength)
    

