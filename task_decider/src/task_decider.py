class TaskDecider:
    def __init__(self,description):
        self.description = description

    def task_decider(self, task_1, task_2):
        while task_1 == "Wash Dishes":
            if task_2 == "Cook Dinner":
                return "Wash Dishes"
            else:
                return "Clean Windows"
        
        while task_1 == "Cook Dinner":
            if task_2 == "Wash Dishes":
                return "Wash Dishes"
            else:
                return "Cook Dinner"
        
        while task_1 == "Clean Windows":
            if task_2 == "Wash Dishes":
                return "Clean Windows"
            else:
                return "Cook Dinner"

        