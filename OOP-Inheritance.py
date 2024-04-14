class classmates:
    def __init__(self, name, age, livingplace, hobby, fav_color):
        self.name = name
        self.age = age
        self.livingplace = livingplace
        self.hobby = hobby
        self.fav_color = fav_color
    def __str__(self):
       return f"{self.name} {self.age} {self.livingplace} {self.hobby} ({self.fav_color})"

p1 = classmates("Fihan", 14, "courtpara", "Anime", "white")
p2 = classmates("Suha", 13, "SonarBangla Mosque", "Drawing", "Violet")
p3 = classmates("Ahnaf", 15, "Fultola", "Cricket", "Black nigga")
p4 = classmates("Shahriar", 13, "P.T.I road", "Gaming", "Green,Black")
p5 = classmates("Tonmoy", 14, "Piyara Tola", "Anime", "blue")
p6 = classmates("Aharnish", 13, "At home", "Cricket", "Brown")
p3.fav_color = "black"
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

