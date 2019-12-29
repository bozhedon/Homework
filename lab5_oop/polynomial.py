class StanfordCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title


print(StanfordCourse)
print(StanfordCourse.mro())
print(StanfordCourse.__init__)

stanford_python = StanfordCourse("CS", "41", "hap.py code: the python programming language")

print(stanford_python.department)  # Print out the department of stanford_python
print(stanford_python.code)  # Print out the code of stanford_python
print(stanford_python.title)  # Print out the title of stanford_python


class StanfordCSCourse(StanfordCourse):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)
        self.is_recorded = recorded


a = StanfordCourse("CS", "106A", "Programming Methodology")
b = StanfordCSCourse("CS", "106B", "Programming Abstractions")
x = StanfordCSCourse("CS", "106X", "Programming Abstractions", recorded=True)
print(a.code)  # => "106A"
print(b.code)  # => "106B"

type(a)
isinstance(a, StanfordCourse)
isinstance(b, StanfordCourse)
isinstance(x, StanfordCourse)
isinstance(x, StanfordCSCourse)
issubclass(x, StanfordCSCourse)
issubclass(StanfordCourse, StanfordCSCourse)
# type(a) == type(b)
# type(b) == type(x)
# a == b
# b == x
