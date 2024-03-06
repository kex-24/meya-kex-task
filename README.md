# Determine the Shape

In this assignment, you will work with Java classes to determine the types of shapes - triangles and rectangles. You will practice using `if` and `else` statements, as well as writing methods to calculate the area of shapes.

### Deadline
This assignment should be completed by the due date of **Friday, 30th September**.

### Instructions
Refer to the course instructions for information on how to complete and submit the assignment.

### Preparation
Make sure to review the course material on object-oriented programming and class design in Java.

### Learning Goals

1. Understanding branching logic (`if` and `else` statements).
2. Implementing class constructors and methods.
3. Utilizing mathematical formulas to calculate areas of shapes.

### Assignment

#### Exercise 1.0 - Triangle Class
Start by creating a new Java class called `Triangle` in the provided `src` directory. The `Triangle` class should have three fields of type `int` representing the sides of the triangle - `side1`, `side2`, and `side3`. Create a constructor for the `Triangle` class that initializes these three sides using three integer parameters.

#### Exercise 1.1 - Valid Triangle Check
Implement a method in the `Triangle` class called `isValidTriangle()` that returns a `boolean` value indicating whether the three sides of the triangle form a valid triangle according to the *triangle inequality* principle. The method should return `true` if the sides can form a triangle, and `false` otherwise.

#### Exercise 1.2 - Triangle Type
Add a method called `getTriangleType()` in the `Triangle` class that returns a `String` representing the type of triangle based on its sides - "Equilateral" for all sides equal, "Isosceles" for two sides equal, and "Scalene" for no sides equal.

#### Exercise 1.3 - Triangle Area Calculation
Now, implement a method `calculateArea()` in the `Triangle` class that calculates the area of the triangle using Heron's formula. You can create a helper method to calculate the semi-perimeter for this calculation.

#### Exercise 2.0 - Rectangle Class
Create a new Java class called `Rectangle` in the `src` directory. The `Rectangle` class should have two fields representing the length and width of the rectangle. Add a constructor to initialize these two fields using integer parameters.

#### Exercise 2.1 - Rectangle Area Calculation
In the `Rectangle` class, implement a method called `calculateArea()` that calculates the area of the rectangle by multiplying its length and width.

### Checklist
- [ ] Create the `Triangle` class with required fields and methods.
- [ ] Implement the `isValidTriangle()` method in the Triangle class.
- [ ] Add the `getTriangleType()` method to determine the type of triangle.
- [ ] Write the `calculateArea()` method in the Triangle class.
- [ ] Create the `Rectangle` class with necessary fields and methods.
- [ ] Implement the `calculateArea()` method in the Rectangle class.

If you encounter any bugs or issues while working on this assignment, please submit a new issue with a detailed description. 

This exercise was modeled after an original task created by [Your Name] ([your.email@domain.com](mailto:your.email@domain.com)), Education Assistant.
# Determine the Shape\n\nIn this assignment, you will work with Java classes to determine the types of shapes - triangles and rectangles. You will practice using `if` and `else` statements, as well as writing methods to calculate the area of shapes.\n\n### Deadline\nThis assignment should be completed by the due date of **Friday, 30th September**.\n\n### Instructions\nRefer to the course instructions for information on how to complete and submit the assignment.\n\n### Preparation\nMake sure to review the course material on object-oriented programming and class design in Java.\n\n### Learning Goals\n\n1. Understanding branching logic (`if` and `else` statements).\n2. Implementing class constructors and methods.\n3. Utilizing mathematical formulas to calculate areas of shapes.\n\n### Assignment\n\n#### Exercise 1.0 - Triangle Class\nStart by creating a new Java class called `Triangle` in the provided `src` directory. The `Triangle` class should have three fields of type `int` representing the sides of the triangle - `side1`, `side2`, and `side3`. Create a constructor for the `Triangle` class that initializes these three sides using three integer parameters.\n\n#### Exercise 1.1 - Valid Triangle Check\nImplement a method in the `Triangle` class called `isValidTriangle()` that returns a `boolean` value indicating whether the three sides of the triangle form a valid triangle according to the *triangle inequality* principle. The method should return `true` if the sides can form a triangle, and `false` otherwise.\n\n#### Exercise 1.2 - Triangle Type\nAdd a method called `getTriangleType()` in the `Triangle` class that returns a `String` representing the type of triangle based on its sides - \"Equilateral\" for all sides equal, \"Isosceles\" for two sides equal, and \"Scalene\" for no sides equal.\n\n#### Exercise 1.3 - Triangle Area Calculation\nNow, implement a method `calculateArea()` in the `Triangle` class that calculates the area of the triangle using Heron's formula. You can create a helper method to calculate the semi-perimeter for this calculation.\n\n#### Exercise 2.0 - Rectangle Class\nCreate a new Java class called `Rectangle` in the `src` directory. The `Rectangle` class should have two fields representing the length and width of the rectangle. Add a constructor to initialize these two fields using integer parameters.\n\n#### Exercise 2.1 - Rectangle Area Calculation\nIn the `Rectangle` class, implement a method called `calculateArea()` that calculates the area of the rectangle by multiplying its length and width.\n\n### Checklist\n- [ ] Create the `Triangle` class with required fields and methods.\n- [ ] Implement the `isValidTriangle()` method in the Triangle class.\n- [ ] Add the `getTriangleType()` method to determine the type of triangle.\n- [ ] Write the `calculateArea()` method in the Triangle class.\n- [ ] Create the `Rectangle` class with necessary fields and methods.\n- [ ] Implement the `calculateArea()` method in the Rectangle class.\n\nIf you encounter any bugs or issues while working on this assignment, please submit a new issue with a detailed description. \n\nThis exercise was modeled after an original task created by [Your Name] ([your.email@domain.com](mailto:your.email@domain.com)), Education Assistant.