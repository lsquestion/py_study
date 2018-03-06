#coding=utf-8

from collections import namedtuple
from collections import deque
from collections import defaultdict

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
#print p.x  表明可以用属性 不需要用索引
#print p.y

q=deque(['a','b','c','d'])


counts=defaultdict(int)

counts['js']=5
print counts



#review :list 列表 可以改变 
#tuple 元组 一旦初始化就不能改变(实质是其每个元素的指向不变.)