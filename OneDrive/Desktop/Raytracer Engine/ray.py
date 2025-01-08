import math
from vector import Vector

class Ray:
    #origin: is a Vector object
    #dir: is a Vector object
    def __init__(self, origin, dir):
        self.origin=origin
        self.dir=dir

    def sphere_intersections(self, sphere):
        radius=sphere.radius
        centre=sphere.centre
        origin=self.origin
        #print(origin.describe())
        dir=self.dir
        print("dir size:", dir.magnitude())
        #print(dir.describe())
        a=dir.dot_prod(dir)
        b=2*(dir.dot_prod(origin)-centre.dot_prod(dir))
        c=origin.dot_prod(origin)+centre.dot_prod(centre)-radius**2-2*centre.dot_prod(origin)

        discriminant=b**2-4*a*c

        # print(f'b^2: {b**2}, 4ac: {4*a*c}')
        # print(discriminant)

        dist=origin.distance_between(centre)

        if discriminant<0:
            print("end 1")
            return Intersection()
        if discriminant==0:
            root=-dir.dot_prod(origin)/dir.dot_prod(dir)
            if root<0:
                print("end 2")
                return Intersection()
            intersection=origin.add_vectors(dir.scale(root))
            print('end 3')
            return Intersection(True, False, [intersection], [root*dir.magnitude(), -1])
        else:
            root1=(-b+math.sqrt(discriminant))/(2*a)
            root2=(-b-math.sqrt(discriminant))/(2*a)
            print("roots:", root1, root2)   
            if dist<radius or ((root1<0 and root2>0) or (root1>0 and root2<0)):
                intersection=origin.add_vectors(dir.scale(max(root1, root2)))
                print('end 4')
                return Intersection(True, True, [intersection], [max(root1, root2)*dir.magnitude(), -1])
            if (root1<=0 and root2<=0):
                print('end 5')
                return Intersection()
            if (root1>=0 and root2>=0):
                intersection1=origin.add_vectors(dir.scale(root1))
                intersection2=origin.add_vectors(dir.scale(root2))
                print('end 6')
                return Intersection(True, False, [intersection1, intersection2], [root1*dir.magnitude(), root2*dir.magnitude()])
    

    def closest_sphere(self, list_of_spheres):
        distances=[]
        min_dist=math.inf
        closest_sphere=None
        for i, val in enumerate(list_of_spheres):
            if self.sphere_intersections(val).exists!=False:
                print(f'{i}th sphere: {val.describe()}')
                distances.append(self.sphere_intersections(val).get_closest_intersection())
            else:
                distances.append([-1])
        print("distances:", distances)
        for i, val in enumerate(distances):
            if val[0]>=0:
                if val[0]<=min_dist:
                    min_dist=val[0]
                    closest_sphere=list_of_spheres[i]

        return [closest_sphere, min_dist]
    
    def contact(self, sphere, light_source, bg_colour):
        if self.sphere_intersections(sphere).get_closest_intersection()[0]<0:
            return bg_colour
        return bg_colour.addcolour(light_source.colour)
    
    def reflect(self, sphere_info, light_source, bg_colour):
        self.contact(sphere_info[0], light_source, bg_colour)
    
    def trace_ray(self, spheres, max_bounces, bounce_count, bg_colour, light_source):
        closest=self.closest_sphere(spheres)
        if closest[0]==None:
            return bg_colour
        colour_hit=self.contact(closest, light_source, bg_colour)
        if bounce_count>max_bounces:
            return colour
        self.reflect(closest, light_source, bg_colour)
        colour=colour_hit+self.trace_ray(spheres, max_bounces, bounce_count+1, bg_colour, light_source)
        


class Intersection:
    def __init__(self, exists=False, inside=False, points=[], distances=[]):
        #points: list of Vector objects, denoting the (x, y, z) coordinates of intersections with an object
        self.exists=exists
        self.inside=inside
        self.points=points  
        self.distances=distances

    def get_closest_intersection(self):
        if self.exists==False:
            return [-1, False, None]
        else:
            if len(self.points)==1:
                return [self.distances[0], self.inside, self.points[0]]
            if self.distances[0]<self.distances[1]:
                return [self.distances[0], self.inside, self.points[0]]
            return [self.distances[1], self.inside, self.points[0]]
# test_ray=Ray(Vector(-0.21, -3.17, 2.32), Vector(-1.87, -1.55, 1.13))
# test_sphere=Sphere(Vector(4.16, 1.96, -3.7), 3, "matte", (255, 255, 255), 1)

# test_vector=Vector(5, 5, 5)
# print(test_vector.dot_prod(test_vector))

# print(test_ray.sphere_intersections(test_sphere))

# print(test_ray.sphere_intersections(test_sphere).points[0])
# print(test_ray.sphere_intersections(test_sphere).points[1])

# print(test_ray.sphere_intersections(test_sphere).get_closest_intersection())



#print("closest sphere", closest_obj.describe())

#print(test_ray_2.sphere_intersections(closest_obj).get_closest_intersection())


