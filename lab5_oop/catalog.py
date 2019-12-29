class StanfordCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title

    def __repr__(self):
        return '{}'.format(self.department)


stanford_courses = [StanfordCourse("CS", "41", "hap.py code: the python programming language"),
                    StanfordCourse("PM", "23", "blablabla"),
                    StanfordCourse("OK", "322", "azaza")]


class CourseCatalog:
    def __init__(self, courses):
        self.courses = courses

    def courses_by_department(self, department_name):
        return [course for course in self.courses if course.department == department_name]

    def courses_by_search_term(self, search_snippet):
        return [course for course in self.courses if search_snippet in course.title]


katalog = CourseCatalog(stanford_courses)

print(katalog.courses_by_department('CS'))
print(katalog.courses_by_search_term('aza'))
