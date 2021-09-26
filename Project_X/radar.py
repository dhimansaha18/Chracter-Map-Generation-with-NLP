# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:35:22 2020

@author: KRISHNA
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    class RadarAxes(PolarAxes):
        name = 'radar'
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def draw(self, renderer):
            """ Draw. If frame is polygon, make gridlines polygon-shaped """
            if frame == 'polygon':
                gridlines = self.yaxis.get_gridlines()
                for gl in gridlines:
                    gl.get_path()._interpolation_steps = num_vars
            super().draw(renderer)


        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)


                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

def work(name,val):
    data = [['1', '2', '3', '4', '5', '6'],(name, [val])]
    N = len(data[0])
    theta = radar_factory(N, frame='polygon')
    spoke_labels = data.pop(0)
    title, case_data = data[0]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(top=0.85, bottom=0.05)
    ax.set_rgrids([0])
    ax.set_ylim(0,max(val))#maximum vertex limit maximum 100, minimum 0
    ax.set_title(title,  position=(0.5, 1.1), ha='center')
    for d in case_data:
        line = ax.plot(theta, d)
        ax.fill(theta, d,  alpha=0.25)
    ax.set_varlabels(spoke_labels)
    plt.show()
    fig.savefig("GRAPHS/"+name+".png")
def graphgen(name,dat):
    s=0
    #s=(dat)
    for i in dat:
        s+=i
    nrml=[]
    for i in dat:
        nrml.append(((i/s)*100))
    print(nrml)
    work(name,nrml)
    fle=open("RSRCE/alllist.txt",'a')
    strng=""
    strng=strng+name+" "
    for i in dat:
        strng=strng+str(i)+"+"
    strng=strng[:-1]
    strng+=" "
    for i in nrml:
        strng=strng+str(i)+"+"
    strng=strng[:-1]
    fle.write(strng+"\n")
    fle.close()
#markers=graphgen("abc",[227,112,258,118,167,86])#input radar graph values
#print(markers)