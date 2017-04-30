import time
import string
import datetime

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


class math_operations(object):
    def __init__(self, alpha,beta,gamma,delta):
        self.alpha= alpha
        self.beta = beta
        self.gamma= gamma
        self.delta = delta

    def are_numbers(self):
        if 4>3:
            return True


class add(math_operations):
    def __init__(self, alpha,beta,gamma,delta, zeta):
        math_operations.__init__(self, alpha,beta,gamma,delta)
        self.zeta= zeta

    def whats_the_sum(self):
        if math_operations.are_numbers(self):
            return self.alpha + self.beta + self.gamma + self.delta + self.zeta


class TimeTrigger(Trigger):
    def __init__(self, time_string):
        stripped_time = time.strptime(time_string)
        print(stripped_time)


c= time.strptime('12 Oct 2016 23:59:59', "%d %b %Y %H:%M:%S")
print(c)

d= time.strptime('13 Oct 2016 23:59:59', "%d %b %Y %H:%M:%S")

if d> c:
    print(True)
# 23:59:59