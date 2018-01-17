import abc

class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor):
        pass

class ConcerteElementA(Element):

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcerteElementB(Element):

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


class Visitor(metaClass=abc.ABCMeta):

    @abc.abstractmethod
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    @abc.abstractmethod
    def visit_concrete_element_b(self, concrete_element_b):
        pass

class ConcreteVisitor1(Visitor):

    def visit_concrete_element_a(self, concrete_element_a):
        pass

    def visit_concrete_element_b(self, concrete_element_b):
        pass

class ConcreteVisitor2(Visitor):

    def visit_concrete_element_a(self, concert_element_a):
        pass

    def visit_concrete_element_b(self, concert_element_b):
        pass

def main():
    concrete_visitor_1 = ConcreteVisitor1()
    concert_element_a = ConcerteElementA()
    concert_element_a.accept(concrete_visitor_1)

if __name__ = '__main__':
    main()
