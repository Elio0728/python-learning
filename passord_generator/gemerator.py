#-*- coding:utf-8 -*-
import random
import string

class PasswordGenerator:
    def __init__(self, length,mode):
        self.length = length
        self.mode = mode

    #Avoid numbers and special characters
    def Easy2Say(self):
        #Uppercase letters
        if self.mode==0:
            password = ''.join(random.sample(string.ascii_uppercase,self.length))
            return password
        #Lowercase letters
        elif self.mode==1:
            password = ''.join(random.sample(string.ascii_lowercase,self.length))
            return password

    #Avoid ambiguous characters like l, 1, O, and 0
    def Easy2Read(self):
        #Uppercase letters
        if self.mode==0:
            password = ''.join(random.sample(string.ascii_uppercase+string.digits+string.punctuation,self.length))
            self.BannedCharacters(password,['l','1','O','0'])
            return password
        #Lowercase letters
        elif self.mode==1:
            password = ''.join(random.sample(string.ascii_lowercase+string.digits+string.punctuation,self.length))
            self.BannedCharacters(password,['L','1','o','0'])
            return password

    #Any character combinations like !, 7, h, K, and l1
    def AllCharacters(self):
        if self.mode==0:
            password = ''.join(random.sample(string.ascii_uppercase+string.digits+string.punctuation,self.length))
            return password
        elif self.mode==1:
            password = ''.join(random.sample(string.ascii_lowercase+string.digits+string.punctuation,self.length))         
            return password
    
    def BannedCharacters(self,password,banned_chars):
        for i,char in enumerate(password):
            while char in banned_chars:
                char = random.choice(string.ascii_letters+string.digits+string.punctuation)
            password = password[:i] + char + password[i+1:]
        return password
