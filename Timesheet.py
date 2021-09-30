class Timesheet:
    def __init__(self, date, noofhours, activity, description, status):
        self.date = date
        self.noofhours = noofhours
        self.activity = activity
        self.description = description
        self.status = status

    def display(self):
        print(self.noofhours)

t= Timesheet("2/5/2021" , "8hrs" , "testing", "idk" , "activity")
t.display()


