from math import sqrt, sin, cos

class Vec2:
    # initialization in two different ways
    def __init__(self, x=(0,0), y=None):
        if y is None:
            try:
                if len(x) == 2:
                    self.x = x[0]
                    self.y = x[1]
            except TypeError:
                raise ValueError("Incorrect single-argument instantiation of Vec2")
        else:
            self.x = x
            self.y = y

    # code representation
    def __repr__(self):
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"

    # make Vec2 readable like a list of two elements
    def __len__(self):
        return 2

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Index out of range.")

    # Output as a tuple of integers, necessary for pygame graphics
    def int(self):
        return round(self.x), round(self.y)

    # Check if the vector is nonzero
    # return false if vector is the zero vector, true otherwise
    def __bool__(self):
        return not (self.x == 0 and self.y == 0)

    # == operator overload
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # + operator overload
    # return a new Vec2 that is the vector sum of self and other
    def __add__(self, other):
        return Vec2(self.x + other.x,
                    self.y + other.y)

    # += operator overload
    # mutate self to be the vector sum of self and other
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # - unary operator overload
    # return a new vector that is opposite this one
    def __neg__(self):
        return Vec2(-self.x, -self.y)

    # - operator overload
    def __sub__(self, other):
        return Vec2(self.x - other.x,
                    self.y - other.y)

    # -= operator overload
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    # * operator overload (scalar multiplication)
    def __mul__(self, scalar):
        return Vec2(self.x * scalar,
                    self.y * scalar)

    def __rmul__(self, scalar):
        return Vec2(self.x * scalar,
                    self.y * scalar)

    # *= operator overload
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    # / operator overload (scalar division)
    def __truediv__(self, scalar):
        inv = 1 / scalar
        return Vec2(self.x * inv,
                    self.y * inv)

    # /= operator overload
    def __itruediv__(self, scalar):
        inv = 1 / scalar
        self.x *= inv
        self.y *= inv
        return self

    # @ operator overload (dot product between vectors, returns a scalar)
    def __matmul__(self, other):
        return self.x*other.x + self.y*other.y

    # perpendicular to a vector, rotated counterclockwise by 90 degrees
    def perp(self):
        return Vec2(-self.y, self.x)
    # makes ~ operator equivalent to perp()
    # ~~v is this equivalent to -v
    __invert__ = perp

    # % operator overload (cross product between vectors, returns a scalar, which is the z component of the result)
    # equivalent to self.perp() @ other, or ~self @ other
    def __mod__(self, other):
        return self.x*other.y - self.y*other.x

    # magnitude squared
    def mag2(self):
        return self.x*self.x + self.y*self.y

    # magnitude
    def mag(self):
        return sqrt(self.mag2())

    __abs__ = mag  # overload abs() operator

    # unit vector
    # return a new unit vector in the same direction
    def hat(self):
        if self:
            return self/self.mag()
        else:
            return self.copy()

    # normalize this vector
    def normalize(self):
        if self:
            self /= self.mag()

    # rotation to return a new vector
    # return a new vector with a counterclockwise rotation
    def rotated(self, radians_or_sine, cosine=None):
        if cosine is None:
            radians = radians_or_sine
            s = sin(radians)
            c = cos(radians)
        else:
            s = radians_or_sine
            c = cosine
        return Vec2(c*self.x - s*self.y,
                    s*self.x + c*self.y)

    def change_to(self, other):
        self.x = other[0]
        self.y = other[1]

    def copy(self):
        return Vec2(self)
