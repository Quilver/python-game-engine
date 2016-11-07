from vector import Vector
from math_extra import Math
from utilities import util
import random, pygame
class Collisions():
    def Detect(me, ent):
            from physics_test import SCREENWIDTH, SCREENHEIGHT, screen
            me_Pos = Vector.Add(me.GetPos(), [me.GetVelocity()[0], SCREENHEIGHT-me.GetVelocity()[1]]) # first entity with a predicted pos
            ent_pos     = Vector.Add(ent.GetPos(), [ent.GetVelocity()[0], SCREENHEIGHT-ent.GetVelocity()[1]]) # second entity with a predicted pos
            y_max, y_min, x_max, x_min = me_Pos[1] + (me.Entity.h * 0.5), me_Pos[1] - (me.Entity.h * 0.5),  me_Pos[0] + (me.Entity.w * 0.5), me_Pos[0] - (me.Entity.w * 0.5) # defining edge coordinates for the first entity
            y_max2, y_min2, x_min2, x_max2 = ent_pos[1] + (ent.Entity.h / 2), ent_pos[1] - (ent.Entity.h * 0.5), ent_pos[0] - (ent.Entity.w * 0.5), ent_pos[0] + (ent.Entity.w * 0.5) # defining edge coordinates for the second entity
            y_range   = Math.Clamp((abs(me_Pos[0] - ent_pos[0])) / (0.5 * ent.Entity.w) * ent.Entity.h, 0, ent.Entity.h) * 0.5 # y range (refer to the picture) This defines valid y coordinate range for left and right edge
            y_range_2 = (y_range*0.5) # y range (refer to the picture) This defines valid y coordinate range for top and bottom range
            left  =  (ent_pos[0] >= x_max >= x_min2) and ((ent_pos[1]+y_range >= y_min >= ent_pos[1]-y_range) or (ent_pos[1]+y_range >= y_max >= ent_pos[1]-y_range)) # is something hitting me from the left
            right = (x_max2 >= x_min >= ent_pos[0]) and ((ent_pos[1]+y_range >= y_min >= ent_pos[1]-y_range) or (ent_pos[1]+y_range >= y_max >= ent_pos[1]-y_range)) # is something hitting me from the right
            top    = ((x_min2 <= x_max <= x_max2) or (x_max2 >= x_min >= x_min2)) and ((y_max2 >= y_min >= ent_pos[1] + y_range_2) or (y_max2 >= y_max >= ent_pos[1] + y_range_2)) # is something hitting me from the top
            bottom    = ((x_min2 <= x_max <= x_max2) or (x_max2 >= x_min >= x_min2)) and ((y_min2 <= y_max <= ent_pos[1] - y_range_2) or (y_min2 <= y_min <= ent_pos[1] - y_range_2))# is something hitting me top
            isColliding = left or right or top or bottom
            Collisions.Stuck_Response(me, ent, [isColliding, left, right, top, bottom] ) # just incase something happens
            Collisions.Response(me, ent, [isColliding, left, right, top, bottom]) # respond to the collision
            return isColliding, left, right, top, bottom # return data about the collision
    def Response(me, ent, physdata):
        isColliding, left, right, top, bottom = physdata[0], physdata[1], physdata[2], physdata[3], physdata[4]
        me_Pos  = me.GetPos()
        ent_Pos = ent.GetPos()
        me_Velocity = me.GetVelocity()
        ent_Velocity = ent.GetVelocity()
        vf_x = (me.Mass * me.Velocity[0]) - (ent.Mass * ent.Velocity[0]) / (ent.Mass + me.Mass)
        #if isColliding:
            #print(vf_x)
            #print(me.Mass * me.Velocity[0], ent.Mass * ent.Velocity[0], ent.Mass + me.Mass)
            #me.Velocity[0] = vf_x
            #ent_Velocity[0] = -vf_x
        if left   == True:
            me.SetVelocity([me_Velocity[0] * -0.2, me_Velocity[1]])
        if right  == True:
            me.SetVelocity([me_Velocity[0] * -0.2, me_Velocity[1]])
        if top    ==  True:
            me.SetVelocity([me_Velocity[0] * me.Friction, me_Velocity[1] * -0.2])
        if bottom == True:
            me.SetVelocity([me_Velocity[0] * me.Friction, me_Velocity[1] * -0.2])
    def Stuck_Response(me, ent, physdata):
        isColliding, left, right, top, bottom = physdata[0], physdata[1], physdata[2], physdata[3], physdata[4]
        if isColliding:
            d = Vector.Distance(me.GetRealPos(), ent.GetRealPos())
            if d == 0:
                me.Entity.move_ip([random.randint(-1,1),random.randint(-1,1)])
                me.Entity.move_ip(Vector.Multiply(Vector.Normalize(Vector.Sub(me.GetRealPos(), ent.GetRealPos())),16))
            else:
                dy = 0
                dx = 0
                if top:
                    dy = abs((me.GetPos()[1] - (me.Entity.h * 0.5)) - (ent.GetPos()[1] + (ent.Entity.h * 0.5)))
                elif bottom:
                    dy = -abs((me.GetPos()[1] + (me.Entity.h * 0.5)) - (ent.GetPos()[1] - (ent.Entity.h * 0.5)))
                if left:
                    dx = abs(me.GetPos()[0] + (me.Entity.w * 0.5) - (ent.GetPos()[0] - (ent.Entity.w * 0.5)))
                elif right:
                    dx = -abs(me.GetPos()[0] - (me.Entity.w * 0.5) - (ent.GetPos()[0] + (ent.Entity.w * 0.5)))
                if abs(Vector.Angle(Vector.Sub(me.GetPos(),ent.GetPos()))) == 45:
                    ent.Entity.move_ip([dx,dy])
                else:
                    if left or right:
                        ent.Entity.move_ip([dx,0])
                    elif top or bottom:
                        ent.Entity.move_ip([0,dy])
    def Unpack(table): # loops through all entities and checks for collision with all of them
        for k, v in enumerate(table):
            for k2, v2 in enumerate(table):
                ent_one = table[k]
                ent_two = table[k2]
                if ent_one != ent_two: # don't collide myself with myself
                    Collisions.Detect(ent_one, ent_two)

