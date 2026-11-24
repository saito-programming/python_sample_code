from dog import *

print("ポチは疲れるまで吠え続けます")
pochi = Dog("ポチ")
for _ in range(4):
    print(pochi.bark())

print(pochi.eat())
print(pochi.bark())
