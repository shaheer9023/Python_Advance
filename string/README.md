# Python String Methods Demo

This repository showcases Python scripts demonstrating various string methods. Each script is listed with its code, a brief explanation, and output.

## 1. isalpha.py

**Explanation:** The `isalpha()` method checks if all characters in a string are alphabetic (a-z or A-Z).

```python
# string validation
string="shaheer"
print(string.isalpha())
string="123"
print(string.isalpha())
```

**Output:**

```
True
False
```

## 2. isalnum.py

**Explanation:** The `isalnum()` method checks if all characters in a string are alphanumeric (a-z, A-Z, or 0-9).

```python
# python function for string validation
string="hello"
print(string.isalnum())
# python function for string validation
string="hello123"
print(string.isalnum())
# python function for string validation
string="hello$"
print(string.isalnum())
```

**Output:**

```
True
True
False
```

## 3. strip.py

**Explanation:** The `strip()` method removes specified characters from the start and end of a string.

```python
web="https://www.facebook.com"
print(web.strip("htps:/w."))
```

**Output:**

```
facebook.com
```

## 4. isdigit.py

**Explanation:** The `isdigit()` method checks if all characters in a string are digits (0-9).

```python
# string validation
string="1234"
print(string.isdigit())
string="1.1"
print(string.isdigit())
```

**Output:**

```
True
False
```

## 5. count.py

**Explanation:** The `count()` method returns the number of occurrences of a substring in a string. It can also take a start index.

```python
string1="my name is shaheer"
string2="aa b c d d e e f f g h i j k l mm"
print(string1.count("shaheer"))
print(string2.count("c"))
print(string2.count("f"))
print(string2.count("aa"))
print(string2.count("j"))
print(string2.count("j",25))
```

**Output:**

```
1
1
2
1
1
0
```

## 6. find.py

**Explanation:** The `find()` method returns the index of the first occurrence of a substring, and `rfind()` returns the index of the last occurrence. Returns -1 if not found.

```python
name="my name is shaheer yes i am shaheer"
print(name.find("shaheer")) #index of first shaheer
# rfind
print(name.rfind("shaheer")) #index of last shaheer
# if no index found returns -1
```

**Output:**

```
11
27
```

## 7. join.py

**Explanation:** The `join()` method concatenates characters of a string, inserting a specified separator between them.

```python
name="shaheer"
print(":".join(name))
```

**Output:**

```
s:h:a:h:e:e:r
```

## 8. center.py

**Explanation:** The `center()` method centers a string within a specified width, padding with a given character.

```python
name="my name is shaheer"
friend="my friend name is shoaib"
print(name.center(50,"-"))
print(friend.center(50,"-"))
```

**Output:**

```
----------------my name is shaheer----------------
--------------my friend name is shoaib------------
```
