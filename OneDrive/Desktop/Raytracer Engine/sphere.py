from ray import Ray
from vector import Vector
from colour import Colour
from light import Light

class Sphere:
    def __init__(self, centre, radius, material, colour, id):
        #centre: is a Vector object
        #radius: is a positive number
        #material: is a Material object
        #colour: is a Colour object
        self.id=id
        self.centre=centre
        self.radius=radius
        self.material=material
        self.colour=colour

    def describe(self):
        print(f'id: {self.id}, center: {self.centre.describe()}, radius: {self.radius}')
    def intersects(self, ray):
        intersection=ray.sphere_intersections(self).get_closest_intersection()

        return intersection
        
    def normal_at(self, vector):
        return vector.subtract_vectors(self.centre).normalize()
    
    def illuminate(self, lights, spheres, point):
        colour=self.colour
        for i, val in enumerate(lights):
            shadow_ray=Ray(val.position, point.subtract_vectors(val.position))
            closest_obj=shadow_ray.closest_sphere(spheres)
            print(closest_obj[0].describe())
            print(closest_obj[1])
            if closest_obj[1]/shadow_ray.dir.magnitude()>1:
                colour=colour.scalecolour(0.01)
            else:
                colour=colour.addcolour(val.lambert_light(self, colour, point, val.colour))
        return colour



