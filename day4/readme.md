# Sneaky Extra Skill
You can jazz things up even more by changing the color of the text. Wow. We're quickly approaching the quality of output of a computer from 1981! 😬
--

#### How does it work?
It's all just `print` statements, but using special codes that tell your console to start printing everything after this point in the new color.
You will need to reset if you want to go back and change it in previous lessons.
 
![image](https://user-images.githubusercontent.com/72098281/211164164-a085093e-16cf-4cc6-9574-dfc530648d98.png)

The somewhat random characters in the print argument are telling the computer to change the color of the next text output to whichever color you pick.

> You must add the number from the table below.

|Color	|Value|
|-------|-------|
|Default|	0|
|Black	|30|
|Red	|31|
|Green	|32|
|Yellow	|33|
|Blue|	34|
|Purple|	35|
|Cyan|	36|
|White|	37|

#### Example
```py
print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
```
![image](https://user-images.githubusercontent.com/72098281/211164408-b15c72d6-5d2c-4c11-837a-64ef3145d925.png)
