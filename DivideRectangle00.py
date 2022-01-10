#original code from "https://medium.com/generative-design/recursive-systems-5b1f813b2b8b"

import Rhino.Geometry as rh
import ghpythonlib.components as ghcomp
def divide(plane, inputCurve, params):
    if len(params) <= 0:
        return []
    
    param = params.pop(0)
    
    curves = []
    lines = ghcomp.Explode(inputCurve)[0]
    pts = [ ghcomp.DivideCurve(line,2)[0] for line in lines ]
    
    if param == 1:
        curves.append(rh.Rectangle3d(plane, pts[0][0], pts[2][1]))
        curves.append(rh.Rectangle3d(plane, pts[0][1], pts[2][0]))
        print curves
        return curves + divide(plane, curves[0], params) + divide(plane, curves[1], params)
    elif param == 2:
        curves.append(rh.Rectangle3d(plane, pts[1][0], pts[3][1]))
        curves.append(rh.Rectangle3d(plane, pts[1][1], pts[3][0]))
        print curves
        return curves + divide(plane, curves[0], params) + divide(plane, curves[1], params)
    else:
        return []
pl = rh.Plane(rh.Point3d(0,0,0), rh.Vector3d(0,0,1))
rect = rh.Rectangle3d(pl, 10, 10)
a = [rect] + divide(pl, rect, params)
