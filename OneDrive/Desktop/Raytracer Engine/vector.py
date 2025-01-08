import math

class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    def describe(self, caption=""):
        print(f"{caption} x: {self.x}, {caption} y: {self.y}, {caption} z: {self.z}")

    def add_vectors(self, v, inplace=False):
        if inplace:
            self.x+=v.x
            self.y+=v.y
            self.z+=v.z
            return self
        else:
            return Vector(self.x+v.x, self.y+v.y, self.z+v.z)
    
    def reverse(self, inplace=False):
        if inplace:
            self.x=-self.x
            self.y=-self.y
            self.z=-self.z
        return Vector(-self.x, -self.y, -self.z)
        
    def subtract_vectors(self, v, inplace=False):
        return self.add_vectors(v.reverse(), inplace)
    
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def scale(self, scalar, inplace=False):
        if inplace:
            self.x=scalar*self.x
            self.y=scalar*self.y
            self.z=scalar*self.z
            return self
        return Vector(scalar*self.x, scalar*self.y, scalar*self.z)

    def distance_between(self, v):
        return math.sqrt((self.x-v.x)**2+(self.y-v.y)**2+(self.z-v.z)**2)
    
    def dot_prod(self, v):
        return self.x*v.x+self.y*v.y+self.z*v.z

    def angle_between(self, v):
        return math.acos(self.dot_prod(v)/(self.magnitude()*v.magnitude()))
    
    def cross_prod(self, v):
        return Vector(self.y*v.z-self.z*v.y, self.z*v.x-self.x*v.z, self.x*v.y-self.y*v.x)
    
    def matrix_multiply(self, matrix, inplace=False):
        if inplace:
            self.x=self.dot_prod(matrix[0])
            self.y=self.dot_prod(matrix[1])
            self.z=self.dot_prod(matrix[2])
            return self
        else:
            return Vector (self.dot_prod(matrix[0]), self.dot_prod(matrix[1]), self.dot_prod(matrix[2]))
    
    def rotate_x(self, angle_x, inplace=False):
        return self.matrix_multiply([Vector(1, 0, 0), Vector(0, math.cos(angle_x), -math.sin(angle_x)), Vector(0, math.sin(angle_x), math.cos(angle_x))], inplace)
    
    def rotate_y(self, angle_y, inplace=False):
        return self.matrix_multiply([Vector(math.cos(angle_y), 0, math.sin(angle_y)), Vector(0, 1, 0), Vector(-math.sin(angle_y), 0, math.cos(angle_y))], inplace)
    
    def rotate_z(self, angle_z, inplace=False):
        return self.matrix_multiply([Vector(math.cos(angle_z), -math.sin(angle_z), 0), Vector(math.sin(angle_z), math.cos(angle_z), 0), Vector(0, 0, 1)], inplace)
    
    def rotate(self, angle_x, angle_y, angle_z, inplace=False):
        return self.rotate_x(angle_x, inplace).rotate_y(angle_y, inplace).rotate_z(angle_z, inplace)
    
    def normalize(self, inplace=False):
        if self.magnitude()==0:
            return self
        return self.scale(1/self.magnitude(), inplace)

    def projection(self, line):
        scalar_prod=self.dot_prod(line.normalize())
        return line.normalize().scale(scalar_prod)
    
    def reflection(self, line, inplace=False):
        return self.subtract_vectors(self.projection(line).scale(2), inplace)
    
    def light_distances(self, list_of_lights):
        distances=[]
        lights=[]
        for i, val in enumerate(list_of_lights):
            distances.append(self.subtract_vectors(val.position).magnitude())
            lights.append(val)
        min_dist=min(distances)
        min_light=lights[distances.index(min_dist)]
        return distances, lights, min_dist, min_light
    
    def colour_scale(self, vector):
        return Vector(self.x*vector.x, self.y*vector.y, self.z*vector.z)
    
    def equality(self, vector):
        if (self.x==vector.x and self.y==vector.y and self.z==vector.z):
            return True
        return False
    
        

v1=Vector(2, 3, 4)
v2=Vector(1, 4, 2)
v3=v1.cross_prod(v2)

print(f"{v1.dot_prod(v2)}")
print(f"{v1.angle_between(v2)}")
print(f"{v3.angle_between(v2)}")
v1.rotate(math.pi/2, 3*math.pi/2, 0, False).describe()
v1.rotate_x(math.pi/2, False).describe()
v1.rotate_y(math.pi/3, False).describe()
v1.rotate_z(37, False).describe()

origin=Vector(-1, -1, -1)
dir=Vector(501, 300, 300)

print(origin.dot_prod(dir))


