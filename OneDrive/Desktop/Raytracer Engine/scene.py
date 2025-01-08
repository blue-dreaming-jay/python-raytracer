from ray import Ray
from colour import Colour
from sphere import Sphere
from vector import Vector
from light import Light
import pygame
import math
from pygame.locals import *
from pygame import gfxdraw
from pygame import Color

class Scene:
    def __init__(self, objects, point_light_sources, bg_colour, ambient_lights, width, height, eye_position):
        #objects should be a list of objects in scene (for now, spheres)
        #point_light_sources should a list of point light sources
        #bg_colour should be Colour object
        #width, height should be integer values
        #eye_position should be a Vector object
        #scene is rendered in 2D, and the plane is considered to be the x, y plane. so all pixels default to z-coordinate of 0
        self.objects=objects
        self.point_light_sources=point_light_sources
        self.bg_colour=bg_colour
        self.ambient_lights=ambient_lights
        self.height=height
        self.width=width
        self.eye_position=eye_position
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def update(self):
        #render the objects and stuff
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()   
    def render_scene(self):
        red=[]
        for x in range(self.width):
            for y in range(self.height):
                primary_ray=Ray(self.eye_position, Vector(500, x, y).subtract_vectors(self.eye_position))
                print('coordinates', x, y)
                closest_obj=primary_ray.closest_sphere(self.objects)
                colour=self.bg_colour
                if closest_obj[0]!=None:
                    intersection=primary_ray.sphere_intersections(closest_obj[0]).get_closest_intersection()[-1]
                    colour=closest_obj[0].illuminate(self.point_light_sources, self.objects, intersection)
                    print(type(colour.to_tuple(255)), colour.to_tuple(255))
                    red.append([x, y])
                gfxdraw.pixel(self.screen, x, y, colour.to_tuple(255))
        print(red)
                
objects=[Sphere(Vector(250, 250, 150), 	40, "matte", Colour(255, 100, 100), 1), Sphere(Vector(100, 100, 100), 30, "matte", Colour(100, 100, 255), 2)]
point_light_sources=[Light(2, Vector(2.53, 6.11, 0), Colour(0, 0, 255), 1,90), Light(1, Vector(500, 0, 0), Colour(255, 255, 255), 1, 90)]
scene=Scene(objects, point_light_sources, Colour(0, 0, 0), [], 600, 600, Vector(-100, 100, 100))
scene.render_scene()
while True:
	scene.update()
		#iterate through each pixel and throw out a ray (primary ray: determine it from eye position to pixel position)
        #check for the closest intersection
        #cast shadow rays from the intersection to the closest light source, check if it hits anything. if it does, you get a shadow
        #actually you can check also if the point is close to light ray intersections. we need colours friends
        #if that shadow ray hits something before the light, then a shadow is cast
        #also the steeper the ray, the darker it should scale (base it off of angle)
        