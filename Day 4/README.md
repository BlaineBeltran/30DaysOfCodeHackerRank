## Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

## Tasks
Write a Person class with an instance variable, **age***, and a constructor that takes an integer, ***initialAge***, as a parameter. The constructor must assign ***initialAge*** to ***age*** after confirming the argument passed as ***initialAge*** is not negative; if a negative argument is passed as ***initialAge***, the constructor should set ***age*** to **0** and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
1. yearPasses() should increase the ***age*** instance variable by **1**.
 amIOld() should perform the following conditional actions:
    - If <img src="https://user-images.githubusercontent.com/55524257/90151146-076c1c00-dd4c-11ea-89b9-a7c79679c065.gif" />, print You are young..
    - If <img src="https://user-images.githubusercontent.com/55524257/90151318-35516080-dd4c-11ea-8450-8cd3b6d4db12.gif" /> and <img src="https://user-images.githubusercontent.com/55524257/90151581-79446580-dd4c-11ea-8d25-3c3b863a0e8f.gif" />, print You are a teenager..
    - Otherwise, print You are old..
## Note:



## Input Format
Input is handled for you by the stub code in the editor.
The first line contains an integer, ***T*** (the number of test cases), and the ***T*** subsequent lines each contain an integer denoting the ***age*** of a Person instance.

## Output Format
Print the total meal cost, where ***totalCost*** is the rounded integer result of the entire bill (***mealCost*** with added tax and tip).

## Constraints
- <img src="https://user-images.githubusercontent.com/55524257/90151875-d2ac9480-dd4c-11ea-9d1f-6bf5be2da44f.gif" />
- <img src="https://user-images.githubusercontent.com/55524257/90152033-f96acb00-dd4c-11ea-8209-4f710c6a9456.gif" />


## Output Format
Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print **2** or **3** lines (depending on whether or not a valid ***initialAge*** was passed to the constructor).
## Sample Input
```python
4
-1
10
16
18
```
## Sample Output
```python
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
```
## Explanation
<img width="858" alt="Screen Shot 2020-08-13 at 10 12 55 AM" src="https://user-images.githubusercontent.com/55524257/90152583-9463a500-dd4d-11ea-96bd-902377ab1d84.png"/>