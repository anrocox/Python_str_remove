#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

In python how to remove a substring of string?

En python ¿como eliminar un substring del string?
'''

#create a str
s = 'red lorry, yellow lorry, red lorry, yellow lorry'
print(s)

#the strings are immutable, so you can not remove substrings
#can use the replace() method if needs to remove a substring regardless of the
#amount of times that repeat in the string.
s_new = s.replace('lorry', '')
print(s_new)

#using merge of strings with the + operator to remove an substring,
#create new string.
s_new = s[:18] + s[23:]
print(s_new)
