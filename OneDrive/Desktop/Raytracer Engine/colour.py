
class Colour:
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b

    def addcolour(self, colour):
        return Colour((self.r+colour.r)/2, (self.g+colour.g)/2, (self.b+colour.b)/2)
    
    def scalecolour(self, scale, returntype="colour"):
        if returntype=="list":
            return [round(min(scale*self.r, 255)), round(min(scale*self.g, 255)), round(min(scale*self.b, 255))]
        else:
            return Colour(round(min(scale*self.r, 255)), round(min(scale*self.g, 255)), round(min(scale*self.b, 255)))
    
    def colour_prod(self, colour):
        return Colour(min(self.r*colour.r, 255), min(self.g*colour.g, 255), min(self.b*colour.b, 255))
    
    def to_tuple(self, alpha):
        colour= (self.r, self.g, self.b, alpha)
        return colour
    

    