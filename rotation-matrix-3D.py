#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : rotation-matrix-3D.py
# Version : 1.0.1
# Python  : 3.5.3
# Blender : 2.78a
# License : MIT
# Author  : Gerard Bajona
# Created : 29/11/2017
# Changed : 30/11/2017
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""
This script is an implementation of the rotation matrix formula in
three dimensions for basic rotations. Check the following URL:
https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations

Sky Texture is a Blender feature to change the sky color according to the Sun
rotation. However, if you add a lamp of type Sun you will have the Sun rotation
pointing to one direction and the Sky Texture painting the Sky for another
solar light direction. So this script will update the Sky Texture according to
the Sun rotation and its solar light direction, automatically.

Name of the lamp        : 'SunLamp'
Name of the world       : 'World'
Name of the Sky Texture : 'Sky Texture'

Usage: rotate the Sun and run this script. Now the color of the sky gets the
color it should have according to the Sun rotation.
"""

import bpy
import mathutils
import math

xAng = bpy.data.objects['SunLamp'].rotation_euler[0]
yAng = bpy.data.objects['SunLamp'].rotation_euler[1]
zAng = bpy.data.objects['SunLamp'].rotation_euler[2]

vec = mathutils.Vector((0.0, 0.0, 1.0))

xMat = mathutils.Matrix(((1.0, 0.0, 0.0), (0.0, math.cos(xAng), -math.sin(xAng)), (0.0, math.sin(xAng), math.cos(xAng))))
yMat = mathutils.Matrix(((math.cos(yAng), 0.0, math.sin(yAng)), (0.0, 1.0, 0.0), (-math.sin(yAng), 0.0, math.cos(yAng))))
zMat = mathutils.Matrix(((math.cos(zAng), -math.sin(zAng), 0.0), (math.sin(zAng), math.cos(zAng), 0.0), (0.0, 0.0, 1.0)))

vec = xMat * vec
vec = yMat * vec
vec = zMat * vec

bpy.data.worlds['World'].node_tree.nodes['Sky Texture'].sun_direction = vec
