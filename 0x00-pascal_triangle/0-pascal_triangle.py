#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        # Returns an empty list if n <= 0
        return []
    # Start with the first row [1]
    triangle = [[1]]  

    for i in range(1, n):
        # Gets the previous row
        prev_row = triangle[i-1]
        # Starts the current row with 1
        curr_row = [1]

        for j in range(1, i):
            # Computes the values by adding adjacent elements from the previous row
            curr_row.append(prev_row[j-1] + prev_row[j])
         # End the current row with 1
        curr_row.append(1)
        # Add the current row to the triangle
        triangle.append(curr_row)
     # Return the resulting triangle
    return triangle
