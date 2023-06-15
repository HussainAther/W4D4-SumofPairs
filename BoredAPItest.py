#!/usr/bin/env python
# coding: utf-8

# In[1]:


from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    key = "You should:"
    def test_diy(self):
       check = solution("diy",20)
       self.assertIn(self.key,check)
    def test_relax(self):
       check = solution("relaxation",100)
       self.assertIn(self.key,check)
    def test_fail(self):
       check = solution("movie",200)
       key = "Nothing to do!"
       self.assertIn(key,check)
    def test_cooking(self):
       check = solution("cooking",100)
       self.assertIn(self.key,check)

