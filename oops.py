class Course:
    meet_links = {}
    notes = {}
    def __init__(self,name,units):
        self.name = name
        self.units = units    
    def add_notes(self,lecture_no,note):
        if lecture_no not in self.notes:
            self.notes[lecture_no] = note
        else:
            print(f"lecture : {lecture_no} notes is already uploaded")
    def add_meet_link(self,lecture_no,link):
        if lecture_no not in self.meet_links:
            self.meet_links[lecture_no] = link
        else:
            print(f"lecture : {lecture_no} meet links is already uploaded")
    def update_notes(self,lecture_no,note):
        if lecture_no not in self.notes:
            print(f"lecture : {lecture_no} notes is not uploaded")
        else:
            self.notes[lecture_no] = note
    def update_meet_link(self,lecture_no,link):
        if lecture_no not in self.meet_links:
            print(f"lecture : {lecture_no} notes is not uploaded")
        else:
            self.meet_links[lecture_no] = link
    def show_notes(self,lecture_no):
        if lecture_no not in self.notes:
            print(f"lecture : {lecture_no} notes is not uploaded")
        else:
            print(f"{self.notes[lecture_no]}")
    def show_meet_link(self,lecture_no):
        if lecture_no not in self.notes:
            print(f"lecture : {lecture_no} meet link is not uploaded")
        else:
            print(f"{self.units[lecture_no]}")
    def delete_notes(self,lecture_no):
        if lecture_no not in self.notes:
            print(f"lecture : {lecture_no} notes is not uploaded")
        else:
            del self.notes[lecture_no]
    def delete_meet_links(self,lecture_no):
        if lecture_no not in self.meet_links:
            print(f"lecture : {lecture_no} meet link is not uploaded")
        else:
            del self.meet_links[lecture_no]

class User(Course):

    courses = []

    def __init__(self,name):
        self.name = name
    
    def add_course(self,course_name,course_units):
        Course.__init(course_name,course_units)