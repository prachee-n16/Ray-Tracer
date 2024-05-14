import numpy as np

class vec3:
    def __init__(self, e0: float=0.0, e1: float=0.0, e2:float=0.0) -> None:
        self.e = np.array([e0, e1, e2], dtype=float)
    
    @property
    def x(self):
        return self.e[0]
    
    @property
    def y(self):
        return self.e[1]
    
    @property
    def z(self):
        return self.e[2]
    
    def __repr__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __getitem__(self, index):
        return self.e[index]
    
    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def length(self):
        return np.sqrt(length_sqrd())
    
    def length_sqrd(self):
        return np.dot(self.e, self.e)

    def __add__(self, other):
        if (isinstance(other, vec3)):
            return vec3((self.e + other.e)[0], (self.e + other.e)[1], (self.e + other.e)[2])
        else:
            print(f"TypeError: unsupported operand type(s) for +: {type(self)} and {type(other)}")

    def __iadd__(self, other):
        if (isinstance(other, vec3)):
            self.e += other.e
            return self
        else:
            print(f"TypeError: unsupported operand type(s) for +=: {type(self)} and {type(other)}")

    def __sub__(self, other):
        if (isinstance(other, vec3)):
            return vec3((self.e - other.e)[0], (self.e - other.e)[1], (self.e - other.e)[2])
        else:
            print(f"TypeError: unsupported operand type(s) for -: {type(self)} and {type(other)}")

    def __mul__(self, other):
        if (isinstance(other, vec3)):
            return vec3((self.e * other.e)[0], (self.e * other.e)[1], (self.e * other.e)[2])
        elif ((isinstance(other, float) and isinstance(self, vec3)) or (isinstance(self, float) and isinstance(other, vec3))):
            return vec3((self.e*other)[0], (self.e*other)[1], (self.e*other)[2])
        else:
            print(f"TypeError: unsupported operand type(s) for *: {type(self)} and {type(other)}")

    def __imul__(self, other):
        if (isinstance(other, vec3)):
            self.e *= other.e
            return self
        else:
            print(f"TypeError: unsupported operand type(s) for *=: {type(self)} and {type(other)}")
    
    def __truediv__(self, other):
        if (isinstance(other, float)):
            return self * (1/other)
        else:
            print(f"TypeError: unsupported operand type(s) for /: {type(self)} and {type(other)}")

    def __itruediv__(self, other):
        if (isinstance(other, float)):
            self.e /= other
            return self
        else:
            print(f"TypeError: unsupported operand type(s) for /=: {type(self)} and {type(other)}")

def dot(self, other):
    return np.vdot(self.e, other.e)

def cross(self, other):
    return np.cross(self.e, other.e)

def unit_vector(self):
    magnitude = np.linalg.norm(self.e)
    return vec3(self.e[0] / magnitude, self.e[1] / magnitude, self.e[2] / magnitude)

# Alias for class, point
point = vec3