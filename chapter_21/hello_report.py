# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:33:31 2019

@author: 11104510
"""

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')