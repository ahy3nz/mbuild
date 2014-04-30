__author__ = 'sallai'
from mbuild.compound import *
from mbuild.port import *
from copy import copy, deepcopy

class Tile(Compound):

    @classmethod
    def create(cls, ctx={}):
        m = super(Tile, cls).create()

        m.add(C((0, 0, 0)),'c')

        m.add(Port.create(),'top_male_port')
        m.top_male_port.transform(Translation((0,0.5,0)))

        m.add(Port.create(),'left_male_port')
        m.left_male_port.transform(RotationAroundZ(pi/2))
        m.left_male_port.transform(Translation((-0.5,0,0)))

        m.add(Port.create(),'bottom_female_port')
        m.bottom_female_port.transform(Translation((0,-0.5,0)))

        m.add(Port.create(),'right_female_port')
        m.right_female_port.transform(RotationAroundZ(pi/2))
        m.right_female_port.transform(Translation((0.5,0,0)))

        return m

if __name__ == "__main__":
    t = Tile.create()
    print t