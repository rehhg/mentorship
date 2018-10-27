

class Component(object):
    def __init__(self, *args, **kw):
        pass

    def component_function(self):
        pass


class Leaf(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)

    def component_function(self):
        print('some function')


class Composite(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        map(lambda x: x.component_function(), self.children)


c = Composite()
leaf1 = Leaf()
leaf2 = Leaf()
c.append_child(leaf1)
c.append_child(leaf2)
c.component_function()
