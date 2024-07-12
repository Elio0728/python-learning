import gemerator

if __name__ == '__main__':
    password1 = gemerator.PasswordGenerator(8,0)
    print("Easy2Say ",password1.Easy2Say())
    print("Easy2Read ",password1.Easy2Read())
    print("AllCharacters ",password1.AllCharacters())
    print("+++++++++++++++++++++++++++++++++++++++++++")
    password2 = gemerator.PasswordGenerator(8,1)
    print("Easy2Say ",password2.Easy2Say())
    print("Easy2Read ",password2.Easy2Read())
    print("AllCharacters ",password2.AllCharacters())