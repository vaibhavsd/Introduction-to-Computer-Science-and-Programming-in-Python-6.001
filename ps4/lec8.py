# Creating class for handling coordinates
class coordinate (object):
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def distance(self, other):
        x_dist= (self.x-other.x)**2
        y_dist = (self.y - other.y) ** 2
        return (x_dist + y_dist)**0.5

    def __str__(self):
        return "< " + str(self.x) + "," + str(self.y) + " >"


point_a= coordinate(1,2)
point_b= coordinate(4,5)


# print(point_a.distance(point_b))
# print(coordinate.distance(point_b, point_a))
# print(point_a)



# Creating class for handling fractions
class fraction(object):
    # initialize
    def __init__(self, num, den):
        self.num= num
        self.den= den

    # print
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # add
    def __add__(self, other):
        num_add= self.num*other.den + self.den*other.num
        den_add= self.den * other.den
        return fraction(num_add, den_add)

    # subtract
    def __sub__(self, other):
        num_add = self.num * other.den - self.den * other.num
        den_add = self.den * other.den
        return fraction(num_add, den_add)

    # float
    def __float__(self):
        return self.num/self.den

    # inverse
    def inverse(self):
        return fraction(self.den, self.num)


frac_a= fraction(1,4)
frac_b= fraction(3,4)
print(frac_a)
print(frac_a+frac_b)
print(frac_a-frac_b)
print(float(frac_a))
print(frac_a.inverse())


