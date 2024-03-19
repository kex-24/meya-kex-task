# Mumin, start your adventure!

For the second exercise of programming, you are going to practice modeling objects in Java. You are going to acquaint yourself with the components of a Java class.

### Deadline
This work should be completed before the exercise, on **Friday 15th September**.

### Instructions
For instructions on how to do and submit the assignment, please see the
[assignments section of the course instructions](https://gits-15.sys.kth.se/inda-23/course-instructions#assignments).

### Preparation

- Read and answer all questions in Module 2: [Looking Inside Classes](https://qbl.sys.kth.se/sections/dd1337_ht23_programmering_prog/container/looking_inside_classes)
- You can access the OLI material both:
  - via Canvas (see the [OLI Torus SE](https://canvas.kth.se/courses/41415/external_tools/4247) link in the left menu)
  - or directly at this [webpage](https://qbl.sys.kth.se/sections/dd1337_ht23_programmering_prog/container/dd1337__programming)


> **Assistant's Note:** The OLI material and tasks might be slightly out of line this year, so it is ok to read ahead if you did not find all the material.

### Learning Goals

This week's learning goals include:
- Designing Java classes
- Adding instance fields
- Adding a constructor method
- Creating getters and setters
- Using the dot operator
- Printing to the terminal
- Using the `main` method
- Scope (or variable shadowing)

### Troubleshooting Guide
If you have any questions or problems, follow this procedure: 

1. Look at this week's [posted issues](https://gits-15.sys.kth.se/inda-23/help/issues). Are other students asking about your problem?
2. If not, post a question yourself by creating a [New Issue](https://gits-15.sys.kth.se/inda-23/help/issues/new). Add a descriptive title, beginning with "Task *x*: *summary of problem here*"
3. Ask a TA in person during the [weekly lab](https://queue.csc.kth.se/Queue/INDA). Check your schedule to see when the next lab is.

We encourage you to discuss with your course friends, but do not share answers!

### Assignment

In the beautiful and mystical world of Moomin Valley, there exists a variety of fascinating creatures known as Moomins. Your task at hand is to model these delightful creatures in Java! 

The main classes of Moomins you'll be working with are Moomintroll, Snufkin, and Snorkmaiden. Just like the Indamons in the previous task, we want to model these characters using Java classes and objects.

### Exercise 2.0 The Moomin beginning

Create a new Java file called `Moomin.java` in the `src` folder. Define a class, `Moomin`, within it. 

Now, let's move on to creating your very first Moomin. Add the main method provided below to your Moomin class. Then create the variables listed below in the main method and assign the corresponding values.  

- String name : Moomintroll
- int hp (hit points) : 15
- int attack : 6
- int defense : 7
- boolean fainted : false

```java
class Moomin {

    public static void main(String[] args) {
        // Create your variables here!

        // Print information of the assigned values
        System.out.println("This is Moomin: ");
        System.out.println("Name: " + name);
        System.out.println("HP: " + hp);
        System.out.println("Attack value: " + attack);
        System.out.println("Defense value: " + defense);
        System.out.println("Has fainted: " + fainted);
    }
}
```

Test your code and check that everything works before moving on.

### Exercise 2.1 More Moomins

In the previous exercise, you successfully created a Moomin. Now, let's broaden your horizons by creating two additional Moomin characters: Snufkin and Snorkmaiden. Repeat the process as you did for Moomintroll and print the information of all three Moomins to the console.

Continue with the following steps to dive deeper into modeling Moomins:

### Exercise 2.2 Fields

Define five fields for the Moomin class: `String name`, `int hp`, `int attack`, `int defense`, and `boolean fainted`. Make sure not to assign any values to them yet. Create a new Moomin object inside the main method. Make use of the dot operator to access and modify the fields of the Moomin object as needed.

### Exercise 2.3 Getters and Setters

Implement getter and setter methods for all the fields in the Moomin class. Remember to follow the naming convention `getXXX` and `setXXX`, where `XXX` is the name of the field. 

Continue by replacing direct field modification with calls to the getter and setter methods. Test that the modified code still compiles correctly.

### Exercise 2.4 Constructor

Implement a constructor for the Moomin class that initializes all fields when a new Moomin object is created. Use this constructor to create new Moomin instances in the main method and print their information.

### Checklist
- [ ] Create three Moomin objects directly in the main method and display their information to the console; delete this code once the verification is done.
- [ ] Define and use five fields in the Moomin class: `String name`, `int hp`, `int attack`, `int defense`, and `boolean fainted.
- [ ] Create getter and setter methods for all fields, and utilize them to access and modify the Moomins' fields.
- [ ] Implement a constructor method for the Moomin class and create Moomin objects using the constructor only.
- [ ] Check the correctness of the program by looking at the predefined checklist above.

### Bugs and Errors
If you encounter any inconsistencies or errors in this exercise, kindly open a [New Issue](https://gits-15.sys.kth.se/inda-23/help/issues/new) with the title "Task *x* Error: *summary of error here*". Found bugs will be acknowledged in the acknowledgment section.

### Acknowledgment
This task was uniquely designed by:
- [Your Name](mailto:your@email.com)
- [Your Name 2](mailto:your2@email.com)

Proofreading & Bug fixes by:
- [Proofreader Name](mailto:proofreader@email.com)