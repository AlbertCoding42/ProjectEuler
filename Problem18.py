import time


start = time.time()

# Converting triangle text document into 2D array for analysing:

triangle_file = open("triangle.txt", "r")
tri = triangle_file.read()
tri1 = tri.split("\n")
triangle = []
for i in tri1:
    triangle.append(i.split(" "))

# n = (number of rows) - 1
#"triangle.txt" is a 100 row triangle, therefore n = 99
n = 99

def maxPathSum(n, triangle):
    for b in range(0, n):

        parent = int(triangle[n - 1][b])
        test1 = int(triangle[n][b])
        test2 = int(triangle[n][b + 1])

        if test1 > test2:
            test1 += parent
            triangle[n - 1][b] = test1
        elif test2 > test1:
            test2 += parent
            triangle[n - 1][b] = test2
        elif test1 == test2:
            test1 += parent
            triangle[n - 1][b] = test1
    n = n - 1
    if n > 0:
        maxPathSum(n, triangle)
    else:
        return triangle

maxPathSum(n, triangle)

#Prints the maximum path sum for any triangle:

print("Found " + str(triangle[0][0]) + " in")
end = time.time()
print(str(end-start) + " seconds")