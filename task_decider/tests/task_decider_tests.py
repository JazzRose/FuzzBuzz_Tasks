import unittest
from src.task_decider import TaskDecider

class TaskDecider(unittest.TestCase):
    def setUp(self):
        self.task_1 = TaskDecider("Wash Dishes")
        self.task_2 = TaskDecider("Cook Dinner")
        self.task_3 = TaskDecider("Clean Windows")


    def test_prefer_wash_dishes(self):
        self.assertEqual("Wash Dishes",self.task_decider(self.task_1,self.task_2))

    def test_prefer_cook_dinner(self):
        self.assertEqual("Cook Dinner",self.task_decider(self.task_2,self.task_3))

    def test_prefer_clean_windows(self):
        self.assertEqual("Clean Windows", self.task_decider(self.task_3, self.task_1))