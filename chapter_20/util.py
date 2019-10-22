# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:23:46 2019

@author: 11104510
"""

def lines(file):
    '''
    在文件末尾添加空行
    '''
    for line in file:
        yield line
    yield '\n' 
    
def blocks(file):
    '''
    生成文本块，将其包含的所有行合并，并将两端空白删除
    '''
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
            