for item in (1,2,3,4,5):
    for i in ["a", "b"]:
        print(item, i)

for item in range(10, 0, -1):
    print(item)

#continue
while True:
    res = input("say something: ")
    if res == "bye":
        break
    else:
        pass

my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)

picture = [
          [0, 0, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0],
]
for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*" , end = "")
        else:
            print(" ", end = "")
    print('')