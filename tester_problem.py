import csv

def FindSafeTriangle(fileName):
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        points = []
        for line in csv_reader:
            x, y = line
            points.append((float(x), float(y)))
    
    # Calculation of the area of a triangle using Heron's formula
    def area(x1, y1, x2, y2, x3, y3): 
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 
  
    # Get the maximum area triangle
    max_area = 0
    max_triangle = []
    for i in range(len(points)): 
        x1, y1 = points[i] 
          
        for j in range(i + 1, len(points)): 
            x2, y2 = points[j] 
              
            for k in range(j + 1, len(points)): 
                x3, y3 = points[k] 
  
                # Calculate area of triangle formed 
                area_triangle = area(x1, y1, x2, y2, x3, y3) 
  
                # Compare the area with maximum area 
                if area_triangle > max_area: 
                    max_area = area_triangle 
                    max_triangle = [x1, y1, x2, y2, x3, y3] 

    # Write the triangle coordinates to the safetriangle.csv
    with open('safetriangle.csv', 'w', newline='') as csvfile:
        fieldnames = ['X', 'Y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(max_triangle), 2):
            writer.writerow({'X': max_triangle[i], 'Y': max_triangle[i+1]})


def FindSafePolygon(fileName):
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        points = []
        for line in csv_reader:
            x, y = line
            points.append((float(x), float(y)))
            
    # Get the maximum area polygon
    max_area = 0
    max_polygon = []
    for i in range(len(points)): 
        x1, y1 = points[i] 
          
        for j in range(i + 1, len(points)): 
            x2, y2 = points[j] 
              
            for k in range(j + 1, len(points)): 
                x3, y3 = points[k]
                
                # Check if the polygon is convex
                if is_convex(x1, y1, x2, y2, x3, y3):
                    # Calculate area of polygon formed 
                    area_polygon = area(x1, y1, x2, y2, x3, y3) 
                    
                    # Compare the area with maximum area 
                    if area_polygon > max_area: 
                        max_area = area_polygon 
                        max_polygon = [x1, y1, x2, y2, x3, y3] 

    # Write the triangle coordinates to the safepolygon.csv
    with open('safepolygon.csv', 'w', newline='') as csvfile:
        fieldnames = ['X', 'Y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(max_polygon), 2):
            writer.writerow({'X': max_polygon[i], 'Y': max_polygon[i+1]})
                    
                    
def FindSafeSurrounding(fileName):
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        points = []
        for line in csv_reader:
            x, y = line
            points.append((float(x), float(y)))
            
    # Get the minimum area triangle
    min_area = float('inf')
    min_triangle = []
    for i in range(len(points)): 
        x1, y1 = points[i] 
          
        for j in range(i + 1, len(points)): 
            x2, y2 = points[j] 
              
            for k in range(j + 1, len(points)): 
                x3, y3 = points[k]
                
                # Check if the triangle is empty
                if is_empty(x1, y1, x2, y2, x3, y3):
                    # Calculate area of triangle formed 
                    area_triangle = area(x1, y1, x2, y2, x3, y3) 
                    
                    # Compare the area with minimum area 
                    if area_triangle < min_area: 
                        min_area = area_triangle 
                        min_triangle = [x1, y1, x2, y2, x3, y3] 
    
    # If no empty triangle is found, find the two closest points
    if min_area == float('inf'):
        min_distance = float('inf')
        closest_points = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
                if distance < min_distance:
                    min_distance = distance
                    closest_points = [x1, y1, x2, y2]
                    
    # Write the triangle coordinates to the safesurrounding.csv
    with open('safesurrounding.csv', 'w', newline='') as csvfile:
        fieldnames = ['X', 'Y']
        writer = csv
     
    
    
 '''
 ignore
 
 '''

# FindSafeTriangle Program
import csv
import sys

#Function to calculate area of triangle
def area(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

#Function to check if the point is inside the triangle
def isInside(x1, y1, x2, y2, x3, y3, x, y): 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3) 
  
    # Calculate area of triangle PBC  
    A1 = area (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC  
    A2 = area (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = area (x1, y1, x2, y2, x, y) 
      
    # Check if sum of A1, A2 and A3 is same as A
    return (A == A1 + A2 + A3)

#Function to find the largest triangle
def findSafeTri(points_csv):
    # Store coordinates of points in csv file in a list
    points = []
    with open(points_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            points.append(row)

    # Store the coordinates of the largest triangle
    max_points = []
    max_area = 0

    # Iterate through all possible combinations of three points
    for x in range(len(points)): 
        for y in range(x + 1, len(points)): 
            for z in range(y + 1, len(points)): 
                x1, y1 = float(points[x][0]), float(points[x][1])
                x2, y2 = float(points[y][0]), float(points[y][1])
                x3, y3 = float(points[z][0]), float(points[z][1])
                # Calculate area of triangle
                area = area(x1, y1, x2, y2, x3, y3)
                # Check if the triangle is empty
                if (isInside(x1, y1, x2, y2, x3, y3, 0, 0) == False):
                    # Store the coordinates of the largest triangle
                    if (area > max_area): 
                        max_points = [x1, y1, x2, y2, x3, y3]
                        max_area = area

    # Write the coordinates of the largest triangle to a csv file
    with open('safetriangle.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(max_points), 2):
            csv_writer.writerow([max_points[i], max_points[i + 1]])

#Function to find the largest convex polygon
def findSafePoly(points_csv):
    # Store coordinates of points in csv file in a list
    points = []
    with open(points_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            points.append(row)

    # Store the coordinates of the largest convex polygon
    max_points = []
    max_area = 0

    # Iterate through all possible combinations of three points
    for x in range(len(points)): 
        for y in range(x + 1, len(points)): 
            for z in range(y + 1, len(points)): 
                x1, y1 = float(points[x][0]), float(points[x][1])
                x2, y2 = float(points[y][0]), float(points[y][1])
                x3, y3 = float(points[z][0]), float(points[z][1])
                # Calculate area of triangle
                area = area(x1, y1, x2, y2, x3, y3)
                # Check if the triangle is empty
                if (isInside(x1, y1, x2, y2, x3, y3, 0, 0) == False):
                    # Store the coordinates of the largest triangle
                    if (area > max_area): 
                        max_points = [x1, y1, x2, y2, x3, y3]
                        max_area = area

    # Write the coordinates of the largest triangle to a csv file
    with open('safepolygon.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(max_points), 2):
            csv_writer.writerow([max_points[i], max_points[i + 1]])
            
#Function to find the smallest triangle containing the person
def findSafeSurrounding(points_csv):
    # Store coordinates of points in csv file in a list
    points = []
    with open(points_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            points.append(row)

    # Store the coordinates of the smallest triangle containing the person
    min_points = []
    min_area = float('inf')

    # Iterate through all possible combinations of three points
    for x in range(len(points)): 
        for y in range(x + 1, len(points)): 
            for z in range(y + 1, len(points)): 
                x1, y1 = float(points[x][0]), float(points[x][1])
                x2, y2 = float(points[y][0]), float(points[y][1])
                x3
    
    
