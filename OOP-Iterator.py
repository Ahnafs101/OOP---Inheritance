# class number:
#     def __iter__(self):
#         self.n = 1
#         return self
#     def __next__(self):
#         if self.n <= 100:
#             x = self.n
#             self.n += 1
#             return x
#         else:
#             raise StopIteration
# MyValue = number()
# Value = iter(MyValue)

# for x in Value:
#     print(x)            



class number:
    def __iter__(self):
        self.c = 3
        return self
    def __next__(self):
        if self.c <= 100:
            x = self.c
            self.c += 4
            return x
        else:
            raise StopIteration
Value = number()
V = iter(Value)
for x in V :
    print(x)
