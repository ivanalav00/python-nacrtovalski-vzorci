import copy

#razred Prototip, ki bo skrbel za kloniranje objektov
class Prototip(object):

    def kloniraj(self):
        return copy.deepcopy(self)



