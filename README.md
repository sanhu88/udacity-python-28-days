每个对象都占据了计算机内存中的某个空间。创建对象时，Python 会为其分配空间。当引用对象的变量超出范围时，Python 可以通过删除不使用的对象释放该内存空间。

但是并非所有对象都可修改。例如，字符串和整数不能修改udacity-python-28-days

learn Python on Udacity

[toc]

> 在线运行python 推荐网站 https://trinket.io/

> typora  以```开头 + 语言名(即 : python)，开启代码块，按换行键换行 

##	第一部分  turtle

**程序**是面向计算机的一组指令。程序由代码行组成。每行告诉计算机关于这些指令的一个特定细节信息。



###	变量  variable

a connection between a name in the code and some date in computer`s memory





### 赋值 assignment

> ~~~ python
> gorge = turtle.Turtle()
> ~~~

En : connect a name with some data in memory

中：将名称与内存中的数据相关联

等号叫做赋值运算符（assignment operator）

整个语句叫做赋值语句（assignment statement）

PS. 赋值语句右侧的代码始终先发生。（先创建再赋值分配）



### 字符串

单词 `"yellow"` 和 `"green"` 称为**字符串**。*字符串* 或 串 (String) 是由数字、字母、下划线组成的一串字符。它是编程语言中表示文本的数据类型。我们称`"yellow"` 这样一串代码为字符*串*



### 整数

此代码中出现的数字（例如 `1`、`90` 和 `100`）都属于*整数*。**整数**是一个没有分数或小数部分的整数。整数可以是正数、零或负数（例如 `-5`）。



### 列表

`[1, 2, 3, 4, 5]` 和 `[7, 2, 1, 0, 9]` 属于**列表**。在 Python 中，列表放入方括号里，并且用逗号分隔各项。



### 模块 module

a file that has a collection of useful code that we can be used in other Python programs.

> 注意，Python 区分大小写



### 方法 method

a block of code that`s hidden away somewhere else,that  this code has a name and now we can run it but using lines like amy.forword(100)

对叫做*amy*的Turtle对象调用*forword*方法，并为其输入100



### 注释

在代码中，**注释**是针对人类读者的消息。计算机在读取代码时，会忽略注释。在 Python 中，注释行以 `#` 开头

- with() 宽度，笔迹的粗细

- speed()速度，越大越快，0最快

- penup() 起笔，不会有笔迹

- pendown()落笔，重新有笔迹


  #### 注释快捷键

  在大多数代码编辑器中，你都可以使用很方便的键盘快捷键注释掉/取消注释一行代码。在 Mac 系统上，快捷键是 ⌘/。在 Windows 系统上，快捷键是 Ctrl + /。如果你将光标放在一行代码上，并按下此快捷键，编辑器将在代码行开头插入 #。



### 变量 variable

~~~ python
pretty_color = 'lightblue'
~~~



import turtle
mary_color = "purple"
step = 100
degree =72
sides =[1, 2, 3, 4, 5]
mary = turtle.Turtle()
mary.color(mary_color)
for side in sides:
    mary.forward(step)
    mary.right(degree)



### 循环 loop

> for ... in ...

side = [1,2,3,4,5] 列表里可以换成字符串，或者其他数字，甚至不同类型可以混合。只要个数不变，不影响画图。

> ```python
> for side in [1, 2, 3, 4, 5]:
>  amy.forward(100)
>  amy.right(72)
> ```

缩进和顺序很重要，没有缩进，就不执行缩进。

缩进空格数量不对，会提示

> **SyntaxError**
>
> **Line:**6
>
> **Error:**bad input



### 列表和循环

> ~~~python
> lengths =[10,20,30,40,50,60,70]
> for length in lengths:
> 	dizzy.forward(length)
> 	dizzy.right(90)
> ~~~

syntax注意冒号（colon）和缩进（indentation）

#### 夹角

> ~~~python
> import turtle
> 
> builder = turtle.Turtle()
> builder.color("red")
> builder.width(5)
> 
> # Copy the angles variable here!
> angles = [-90, 0, 0, -90,
>        135, 0, 0, 0, 
>        90, 0, 0, 0,
>        135, -90, 0, 0,
>        90, 0, 0, 0]
> for angle in angles:
>  # Turn right, then go forward 25.
>  # (How far to turn?
>  #  Use the angle variable!)
>  builder.right(angle)
>  builder.forward(25)
> ~~~



### 嵌套循环 Nested Loop

~~~python
import turtle
anna = turtle.Turtle()
for path in [1, 2, 3, 4]:
    for step in [1, 2, 3]:
        anna.forward(10)
~~~



### Turtle总结

- 移动

  lola.forward(n) 	前进，可以负数

  lola.back(n)

  lola.speed(s) 	速度，0时最快

- 转向

  lola.right(a) 	右转a度数，可以为负数

  lola.left(a)

- 绘制

  lola.penup() 	抬笔

  lola.pedown()	落笔

- 显示和隐藏

  lola.hideturtle()	隐藏箭头

  lola.showturtle()	取消隐藏



### 三种错误

编程中会出现三大类型的错误：**语法错误**、**用法错误**和**逻辑错误**

#### 语法错误

也就是拼写错误，少了后括号，或者for少了很容易落掉的冒号

#### 用法错误

就是不可以这样使用

~~~python
alison.forward("orange")
~~~

包含Python 的 `NameError` 和 `TypeError` 消息通常都是这种类型的错误。你之前见到的 `ZeroDivisionError` 也算是这种错误。

`NameError` 是一种常见的 Python 错误消息，表示代码在定义变量前尝试使用该变量。例如，如果尚没有叫做 `matthew` 的 turtle，`matthew.right(45)` 将抛出 `NameError`。

#### 逻辑错误

~~~python
import turtle
michael = turtle.Turtle()
for side in [1, 2, 3, 4, 5, 7, 8]:
    michael.forward(100)
    michael.right(45)
~~~

上面for中少了元素6，所以不是八边形

#### 缩进计算

~~~python
willow = turtle.Turtle()
for x in [1, 2, 3]:
    willow.forward(1)
    for y in [4, 5, 6, 7]:
        willow.forward(1)
    willow.forward(1)
~~~

一共前进了多少？

外循环每次进2格，共3次外循环，小计6

内循环每次进1，4次内*3此外，小计12

合计18

答案：由于一个循环在另一个循环里缩进了，因此不同的 `forward` 命令运行了不同的次数。第一个 `forward` 命令运行三次；第二个运行十二次，第三个运行三次。

#### 六边形

> 多边形移动角度，是360除以形状的边数。

***

## 第四课

### statements 语句

##### 简单语句 Simple Satements

* 赋值语句 Assignment Statements

~~~python
pretty_color = "Red"
amy = turtle.Turtle()
~~~

* 导入语句 Import Statements

~~~python
import xxx
~~~

* 调用语句 Call Satements

~~~python
amy.forward(100)
amy.color("Blue")
~~~

##### 复合语句 Compund statements

* for循环

复合语句用来控制Whether / When / How many times to run codes

复合语句包含冒号和缩进

##### 控制流  Control Flow

代码的运行顺序，叫做程序的控制流。复合语句会改变从上到下的控制流。

for循环改变了How Many Times 的控制流



#### range函数

[1,2,3,4] 相当于 range(4)

~~~python
sides = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
range(100)
~~~



#### 数字运算

3 X 4 写成 3 * 4 （asterisk 型号），9 ÷ 3 写成 9 / 3 （slash 斜杠）

##### 表达式 Expression

a piece of code that resolves to some value，解析某个值的一段代码

~~~python
2 + 2
~~~

表达式有两部分，数字和符号（symbols）

operators 运算符和operands运算对象/运算数

<img src=".\screenshots\operators_operands.png" alt="operators_operands" style="zoom: 50%;" />

~~(图片真实存在。如果看不到图片，因为总所周知的原因，你可能要想点办法)~~

图片看不到，更新host试下，[办法连接](https://blog.csdn.net/qq_38232598/article/details/91346392)

###### 变量也可以参与到算数运算符

~~~python
for side in [1, 2, 3, 4]:
    amy.forward(10 * side)
    amy.right(90)
~~~



#### 函数 Function

 range() 是 Python 的一个内置函数 

~~~python
print(range(5))
[0,1,2,3,4]
~~~

##### 调用语句或者调用 call statement or call

~~~python
range(100)	#调用range
~~~

##### argument 参数

~~~python
range(100)	#100即为传递的参数
~~~

调用函数-->传递参数-->返回结果

##### method call 和 function call

```python
amy.forward(100)	#method call
range(100)			#function call
```

方法是是一种特殊的函数，所有方法都是函数。但并非所有的函数都是方法

函数部分知识小结

1. 函数：一块有名字的代码，他在我们调用他之前，不会自主运行 
2. 函数调用 ： 让函数运行的语句
3. 参数 ： 再调用函数时，传递的数值
4. 方法 ： 与对象有关的函数

#### 定义函数

> 定义函数再封装重复使用相同部分的代码



> 必须在调用函数之前定义函数，否则会遇到如下所示的错误：
>
> **Error: name 'draw_square' is not defined**

 函数定义始终以 `def` 开头，然后是函数名称，括号 `()` 和冒号 `:` 

~~~python
def function_name():
    xxxxxxxxxxxxxxxxxxxx
    for _ in range(20):
        XXXXXXXXXXx
        
function_name()
~~~

#### 参数 argument

##### 形参 parameters

定义函数的参数，形式上的

 形参并不是什么高级概念，它就是变量。 

~~~~pytho
def spiral(sides, turn, color, width):
~~~~

##### 实参 argument

调用函数时传入的实际参数

 实参也不是什么高级概念，它只是我们传递给函数的输入 

~~~python
spiral(150, -30, "blue", 10)
~~~

 ##### 传递

当我们提到它“传递”此实参时，是指它将此数字赋值给相应的形参 

因此“向函数传递实参”其实就是向变量赋值的另一种方式 



~~~
#画个正方形
import turtle
jack = turtle.Turtle()
jack.color("yellow")

def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)

draw_square()
~~~



#### 变量范围 variable scope

> 函数定义的变量只能在该函数内使用，局部（内部）变量，local scope

> 全局变量 global scope，在函数外定义

变量来自：

## 变量来自哪里？

很多变量是由赋值语句创建的，例如 `intensity = 10`。但是还可以通过其他方式创建变量。你在这门课程中已经见过很多种方式。

- 每个 `for` 循环都会创建一个变量，例如 `for step in dance:` 中的 `step` 变量。如果该循环在函数内，则该变量是局部变量。
- 每个 `import` 语句都会创建全局变量，然后使用该变量引用导入的模块。例如，语句 `import turtle` 在内存里创建了 *turtle* 模块的副本，并创建一个叫做 `turtle` 的变量，用来引用该数据。然后，当你需要引用该模块时，你可以在代码中使用 `turtle`。换句话说，`import turtle` 语句创建了一个变量，其名称是 `turtle`，值是 turtle 模块本身。
- 每个函数定义都会创建一个变量。函数名称（例如上方的 `bounce` 和 `boogie`）都是变量！创建了这些变量后，我们就可以在之后需要时引用该函数（例如调用函数时）。
- 当函数有形参时，例如上方代码里的 `something`，这些形参是该函数的局部变量。

### 变量的作用域

~~~ python
import turtle

def draw_square(who,length):
  for side in range(4):
    who.forward(length)
    who.right(90)
    
def draw_flower(size,petals):
  doodler = turtle.Turtle()
  doodler.color("orange")
  doodler.width(3)
  doodler.speed(0)
  for petal in range(petals):
    draw_square(doodler,size)
    doodler.right(360/petals)
    
draw_flower(100,99)
~~~

从上到下解读

1. 导入turtle 模块 module【全局】

2. 运行函数定义 draw_squre 【全局】，将函数主体所有代码放入内存，并与之关联、

3. 定义函数 draw_flower【全局】，(代码只是被保存，没有实际运行)

4. 调用函数 draw_flower，size = 100, petals = 99

5. 然后调用turtle 函数 创建Turtle对象，并保存到doodler 变量中

6. 改变doodler 颜色和宽度

7. 进入for循环，range出 0-6的7个数字

8. 调用draw_square全局变量，传入doodler和 100，赋值给形参length 100.

   draw_square 是看不到petals的，因为petals是draw_flower的局部变量

![](.\screenshots\draw_flowers.png)





### 两个Turtle

~~~python
import turtle
romeo = turtle.Turtle()
juliet = turtle.Turtle()
~~~

创建两个不同的 turtle 对象（一个叫做romeo。一个叫juliet）

 那么在内存中有两个不同的底层对象。意味着我们可以单独对这两个对象设置颜色。 



### 同一个Turtle

~~~python
import turtle
romeo = turtle.Turtle()
montague = romeo

montague.color("red")
montague.width(5)

montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)
romeo.color("white")
montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)
~~~

在中间，更改了romeo的颜色，mantague后面的也会改变。

### 函数调用函数

~~~python
import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(romeo)
~~~

调用逻辑如下图

![](.\screenshots\functions-calling-functions.png)

分开写有分开写的好处

 这种方法很常见，因为它有很大的优势。例如，我们可以在这个程序中添加其他的代码，用 `draw_square` 函数来做点别的事情（而不是画花）。通过将不同的任务分解到不同的函数中，可以让代码使用更方便，也更灵活。 

做练习时，我有写在一起的方法，更少的行数，失去了灵活性。

4-23-花瓣_函数调用函数.py

## 第五课 函数 第二部分

### if

~~~python
squids = 17
becky = turtle.Turtle()
becky.color("red")
if squids == 42:
    becky.color("blue")
becky.width(5)
~~~



最后颜色为 red 因为if条件没有满足



### 循环中加入条件判断

~~~python
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
~~~

range(4) 会创建序列 0, 1, 2, 3，所以 side 将在循环的 第四次 时，取值为 3 。



下面这道题做错了

~~~python
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
~~~

> 颜色更改为蓝色（第三条边）后，没有将其改回黄色的代码，因此在画第四条边时，依然是蓝色。 

### if else

~~~python
import turtle
jack = turtle.Turtle()
jack.width(5)


for side in range(4):
    if side == 1:
        jack.color("blue")
    else:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)
~~~



### 模运算 modulo

#### 取余数 %

7 % 2 = 1

7除以3 得2 余1

1%5 = 1

>  我们可以把 1 分成多少组 5 ？在我们把它分成 5 个一组之后还剩下多少？ 

 我们并不能把 1 分成 5 个一组。所以我们有 0 组，每组 5 个，剩下原来的1（余数是1） 

>  如果 `a % b` 中 `b` 更大，那么余数就是 `a` 

> 对于任何数字 y，x % y 的值始终小于 y 本身。

小乌龟画楼梯：

~~~python
import turtle

amy = turtle.Turtle()
amy.speed(0)
amy.width(4)
amy.color("orange")

for _ in range(10):
    amy.forward(20)
    if _ % 2 == 0:
        amy.left(90)
    else:
        amy.right(90)
~~~



 模运算经常与 `for` 和 `if`语句一起使用 

~~~python
for n in range(12):
   if n % 3 == 0:
      draw_triangle()
   else:
      draw_square()
~~~

### 返回值

~~~python
def simple_function():
    return 10

distance = simple_function()
~~~

return 关键字

~~~python
import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number**2

for n in range(540):
    angle = square(n)
    t.right(angle +.5)
    t.forward(5)
~~~

上面代码画出一个很有意思的封闭图形

![](.\screenshots\reture-draw.png)

函数可以返回多个返回语句。但是被调用时，运行到第一个返回语句后就会停止。除非放在判断语句，比如 if else 中

~~~python
import turtle

def super_reptile():
    amy =turtle.Turtle()
    amy.speed(0)
    return amy


clark = super_reptile()
clark.forward(100)
clark.left(45)
clark.forward(100)
# up, up, and away!
~~~



小练习

~~~python
def mystery():
    for word in ["love", "peace", "kittens"]:
        return word
    return "doom"
~~~

上面将返回的时love。 在第一次遍历循环时，`word` 的值是 `"love"`。函数从未遍历列表的剩余部分。`"doom"` 行是无用代码。 

如果改成下面这样

~~~python
def mystery():
    for word in ["love", "peace", "kittens"]:
        #return word
         name =word
    
    return name
print(mystery())
~~~

返回的才是最后一个kittens



### 循环和实参

turtle 上的 `forward` 方法仅接受一个实参：如果 `mark` 是 turtle，那么 `mark.forward(10, 20)` 将出错。

这意味着，如果你更改函数接受的实参数量，还需要更改调用该函数的每一处代码



### 复合语句

 目前为止见过的各种**复合语句**。有三种复合语句：**for** 循环、函数定义 **def** 和 **if** 语句。 

共同特点

-  第一行始终以该语句的关键字开头：`for`、`def` 或 `if` 
-  第一行始终以冒号 `:` 结尾 
-  剩余代码行属于代码块，都按照相同的空格数量缩进 

### random模块

#### 确定性 deterministic program

always products the same output for a give input.

#### **import random**，不导入，会报错

~~~
ameError
Line:12
Error: name 'random' is not defined
~~~



- random.randint 随机选择一个整数，接受两个参数，最小值和最大值.

  ~~~python
  # Roll a six-sided die.
  dieroll = random.randint(1, 6)
  ~~~

  

- random.choice,接受一个参数，必须为列表

~~~python
cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king"]
# Pick a card at random.
mycard = random.choice(cards)
~~~

练习：

~~~python
import turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple","white"]

t = turtle.Turtle()
t.width(4)
t.speed(0)

for step in range(10):
    # Change this to use a random number.
    angle = random.randint(5,150)

    # Change this to use a random color.
    color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(50)

~~~

![image-20200311153500701](README.assets/image-20200311153500701.png)

### 不等式

#### 比较运算符

| **运算** |        **含义**         |
| :------: | :---------------------: |
| `a == b` |    `a` 等于 `b` 吗？    |
| `a < b`  |    `a` 小于 `b` 吗？    |
| `a > b`  |    `a` 大于 `b` 吗？    |
| `a <= b` | `a` 小于或等于 `b` 吗？ |
| `a >= b` | `a` 大于或等于 `b` 吗？ |
| `a != b` |   `a` 不等于 `b` 吗？   |

~~~python
def temperatureColor(temp):
    if temp < 30:
        color = "blue"
    else:
        if temp < 60:
            color = "purple"
        else:
            color = "red"
    return color
~~~



### elif

elif解决了必须if嵌套的代码复杂问题

比如之前写法如下：

~~~python
if mood == "happy":
	amy.color("red")
	else:
		if mood == "sad":
			amy.color("blue")
		else:
			amy.color("gray")
~~~

如果上面都只是写在外面，如下方写法，就会和预计出错

~~~python
if mood == "happy":
	amy.color("red")
if mood == "sad":
	amy.color("blue")
else:
	amy.color("gray")
~~~

因为最后一个else是和第二个if对应的。所以即便mood = "happy",颜色却是gray。

尤其是在多重判断时，会让嵌套变得冗长

使用elif来解决

~~~python
if mood == "happy":
	amy.color("yellow")
elif mood == "sad":
	amy.color("blue")
elif mood == "angry":
	amy.color("red")
else:
	amy.color("gray")
~~~

### 逻辑运算符

and / or运算符

~~~python
if x > 0 and x < 10:
    # Do something
~~~

支持以上写法，都满足条件才运行,而且支持多个联合起来用

~~~python
x > 0 and x < 10 and y > 0 and y < 10
~~~



### Turtle边界问题

xcor ，X coordinate : horizontal value

ycor , Y coordinate : vertical value

来检查tutle的当前位置

~~~python
 t.penup()
 t.home()
 t.pendown()
~~~

home()  将画笔返回到原点 

练习

~~~python
import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    # Add your code here
    if t.xcor() > 20 or t.xcor()< -20:
        t.right(90)
~~~

以上有趣的是

~~~python
 t.right(90)
 和
 t.right(180)
 效果基本一致
~~~



#### 复习

 函数调用 `random.randint(0, 359)` 将返回一个从 `0` 到 `359` 的随机数字，也就是随机整数夹角。不需要达到 `360`，因为转动 `360` 度和一开始的朝向一样，也就是转动 `0` 度。 

random.randint 必须有两个参数

random.randint(range(359))

### 第六 大练习 房贷计算器

遇到的问题点记录

1. 关于平方的计算方式是**。例如等额本息的公式

   ~~~
   monthly_payment = round((P*R*(1+R)**N)/((1+R)**N-1),2)
   ~~~

   

2. print中打印变量是使用%i,%.2f 来绑定

   ~~~python
   print("EPP等额本金:第  %i  月，需要还款 %.2f" %(n, monthly_payment) )
   ~~~





## 第七课  安装Python

>  每版 Python 的版本号都由三部分数字组成，例如 Python 2.7.9 或 Python 3.6.2。版本号的不同部分表示更改幅度有多大。第一个数字表示存在大型改动，第二个和第三个数字表示存在更小型的改动。 

 我们将使用 **Python 3.x**（意味着任何以 **3** 开始的版本都可以）。要获取所有最新功能，建议使用 **Python 3.6** 或更高版本。 

 https://www.python.org/downloads/ 

1. 选择自定义安装
2. 添加python 到环境变量

#### 终端里使用python

- input 函数

~~~python
input("What's your name?")
~~~

一般赋值到变量

~~~python
name = input("What's your name?")
~~~

input 也可以不传入参数

- print 函数

  如果是要直接输出所见，不进行运算，需要加上双引号

  **接受多个参数，以逗号分隔。结果是空格分隔显示**

#### 交互模式 interactive mode

三个大于号 起始

交互模式的代码不会保存

退出 win Ctrl+C / Mac Ctrl+D

##### 复合语句

在交互模式下书写复合语句，

~~~python
>>> for side in range(4):
...
~~~

会显示三个点，留意四个空格缩进。

 要退出循环并运行循环，直接再按一次 Enter 键。 

#### 复习函数

~~~pyth
def confuse():
    print ("bears")
    return 42

confuse()
print(confuse())
~~~

一个直接调用函数，只有打印 bears，如果打印调用的结果，就会有两个bears和42。因为，在交互界面，return不打印，不显示。

 Python 用 `None` 表示没有值 ，如果函数没有返回值，就返回None 不是什么都不返回。如下：

~~~python
def more_confused():
    2 + 2

print(more_confused())

~~~

如果有两个return，只会返回第一个

~~~python
def say_hello():
    return "Hello!"
    return "Goodbye!"

print(say_hello())
'''
只有"Hello!" 会显示
'''
~~~





#### 交互式里的函数

 交互模式下返回值时，该值会显示出来。但是文件里的return不会显示

 这是在交互模式下运行代码的一个好处。任何时候，只要输入语句或表达式，交互模式将显示返回值。这样使你能够更熟悉代码的内部情况。 

 因为交互模式会显示任何返回值（即使没有对这些值执行任何操作）。 

如果是没有return和print 就无任何返回

~~~python
>>> def nothing():
...     2+2
...

~~~

#### 错误类型

操作数和运算符 

~~~python
>>> 2 + "fish"

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
~~~



~~~python
>>> n = input("input a number:")
input a number:4
>>> n
'4'
>>> n+2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>
~~~

input 总是返回string，解决办法格式化

~~~python
n = int(input("Please enter a number:"))
~~~





#### 导入模块

 在导入时，不要在文件名后面添加文件扩展名 。

 注意，和调用 `turtle` 模块里的方法一样。我们需要输入 `turtle.right(90)` 和 `turtle.forward(100)`，而不是直接输入 `right(90)` 和 `forward(100)`。 



~~~python
import antigravity

打开浏览器，默认 https://xkcd.com/353/ 网络漫画
~~~



## 第九课 字符串和列表

#### 变量

变量名 variable name 也叫做标识符 identifier

~~~python
>>> "cake" = "yummy"
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
~~~

Literals 字面量

数字和字符串 没有办法再次赋值，会报错SyntaxError : can`t assign to literal. 因为数字和字符串已经固定了绑定本身，是字面量。

#### 字符串

单引号和双引号，都可以使用，但是必须成对使用。

\n 换行，可以一起使用多个

- 单引号`'`与双引号`“`
- 换行符`\ n`
- 转义符`\`
- 三引号`"""`

单双引号，可以互换再外面，来显示需要显示内部存在的。

如果内容包含两种，

1. 使用反斜杠转义字符。
2. 三引号来包含



练习

~~~python
>>> def print_all(your_list):
...     for li in your_list:
...         print(li,'\n')
~~~

答案

~~~python
def print_all(strings):
    for string in strings:
        print(string)
~~~

 更复杂的字符串

~~~python
'''
"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.

It's long," said the Knight, "but it's very, very beautiful."
'''

print("""\"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.

It's long," said the Knight, "but it's very, very beautiful.\"""")

'''答案
print('"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.\n\n"It\'s long," said the Knight, "but it\'s very, very beautiful."')

答案二
print("""
"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.

"It's long," said the Knight, "but it's very, very beautiful."
""")
'''
~~~

三引号`"""`可以，四引号`""""`不可以！

SyntaxError: EOL while scanning string literal.

问题出在字符串末尾的四个引号`""""`上。Python将**其中的前三个**视为已到达字符串末尾的信号 — 因此，当它随后遇到第四引号时，它认为我们正在开始一个新的字符串。然后我们再也不会关闭该新字符串，这就是导致错误的原因。

#### 复习函数和类型

 `input` 函数始终返回字符串 

~~~python
number = input("Enter a number!")
~~~



 如果你要求 Python 输出无法转换为字符串的对象（例如模块、函数或 turtle），系统就会显示这种带 `<尖括号>` 的消息。但这不是错误消息。 

~~~python
import turtle
print(turtle)

~~~

会返回

~~~python
<module 'turtle' from 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python38\\lib\\turtle.py'>
~~~

#### 长度 len()

起止冒号不计算在内， 字符串中的**所有字符都算在内，包括空格** 

也适用于list [],项目中的数量

~~~python
TypeError: object of type 'int' has no len()
TypeError: object of type 'function' has no len()
~~~

表情符号

~~~python
import unicodedata
>>> unicodedata.lookup("airplane")
~~~

~~~python
>>> len("🐍")
1
>>> len("蛇 = 🐍")
5
~~~

 表情符号在屏幕上的占据空间通常比字母或数字更宽；在等宽字体中，它们通常占据两个字符。并且占据更多计算机内存。但是 Python 字符串的长度仅取决于其中的字符数量，而不是什么类型的字符

#### 遍历字符串

for 可以遍历列表和字符串

~~~python
message = input("What do you have to say, hm?\n")

for ch in message:
    if ch == "?":
        print("Sense much curiosity in you, I do.")
    if ch == "!":
        print("Enthusiastic, you are.")
~~~

#### 字符串计数

在开始计数之前，我们必须分配`count`变量的初始值

~~~python
count = 0
for ch in "bonobos":
    if ch == "o":
        count +=1
print(count)
~~~

~~~python
def count_character(full_srt,search_str):
    count = 0
    for ch in full_srt:
        if ch == search_str:
            count = count + 1
    return(count)



print("Should print a count of 3:")
print(count_character("oxen and foxen all live in boxen", "x"))

print("Should print a count of 0:")
print(count_character("that letter isn't here", "x"))

print("Should print a count of 9:")
print(count_character("the goofy doom of the balloon goons", "o"))

print("Should print a count of 6:")
print(count_character("papa pony and the parcel post problem", "p"))

print("Should print a count of 0:")
~~~



#### 索引 index

字符串和列表都有len()

字符串和列表都是0开始索引

索引运算符 subscript operator /index operator [1]

练习

~~~ python
def start_k(s):
    return s[0] == 'k' or s[0] == 'K'
~~~

留意，以上代码区分大小写

##### 负索引

 如果 `word` 是一个字符串，那么 `word[-1]` 是该字符串的最后一个字符，`word[-2]` 是倒数第二个，等等 

##### 零索引

~~~python
no_words = ""
print(no_words[0])
~~~

上面会返回

> IndexError: string index out of range

~~~python
"apple"[-6]
~~~

也是超出index的范围报错。

练习题

~~~
"Art3mis"[3][0][0] 的值是多少？
~~~

> `"Art3mis"[3]` 的值是字符串 `'3'`。`'3'[0]` 的值也是 `'3'`。
>
> 对于任何非空字符串 `x`，`x[0]` 的值和 `x[0][0]` ... 甚至 `x[0][0][0][0][0]` 一样。

### range 函数

~~~python
>>> for n in range(4):
...     print(n)
0 1 2 3
~~~

当你传递一个数字时，range会给您返回一个序列，该序列**不包括最大的那个数字**。有时你会听到这被描述为**“exclusive”**范围，因为你给出的数字被*“excluded（排除）”*了。

~~~python
 for n in range(1,4):
...     print(n)
...
1
2
3
>>> for n in range(97,101):
...     print(n)
...
97
98
99
100
>>> for n in range(0,10,2):
...     print(n)
...
0
2
4
6
8
~~~

range(起始，终结【不包含】,步长【step】)

~~~python
>>> for n in range(0,10,1.5):
...     print(n)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
~~~



### 超出范围

交互模式错误中会有一个文件名<stdin>的提示

STDIN 代表 standard input 标准输入的简称，也就是是键盘输入产生的

~~~python
no_words = ""
print(no_words[0])

IndexError: string index out of range
~~~



#### Tracebacks（最近的调用在最后）

 当函数调用出现（非语法）错误时，Python 将尝试告诉你导致该错误的整个函数调用流程。 

#### indexError

如何避免索引错误：

1. 不使用索引，直接for chr in word
2. 使用字符串/列表的长度，for n in range(len(word))

### 切片 Slice

截取部分 

~~~python
'apple'[0:3]
#app
~~~

将包含第一个位置开始，一直持续到第二个值（但不包含），从0开始的话，可以省略0

~~~python
'apple'[:3]
~~~



如果第二个值超出剩余长度，则取出剩下全部，并不会报错

~~~python
'balloon'[3:8]
~~~

等同于

~~~python
'ballon'[3:]
~~~

结果都是 loon

~~~python
>>> "presto"[1024:4096]
''
~~~

此表达式将仅包含六个字符的字符串中取出位置从 1024 到 4096 的字符。这看起来像是一定会产生索引错误的代码，但是 Python 只会返回它能取到的一切。它在这些位置上无法获得任何内容，因此仅返回一个空字符串。

#### 特殊情况

 如果 `word` 是一个字符串，`word[:]` 将是 `word` 的副本。 

 如果切片尝试提取字符串末尾之外的字符，将返回至多能获取的字符，即使什么也没有

~~~python
def word_triangle(word):
    # Add your code here
    for n in range(len(word)):
        print(word[:-n])
        
word = input("type a long word : ")
word_triangle(word)
~~~



### 字符串操作

#### 连接

**+号**，可以拼接字符串和空格

不可以拼接字符串和int

前后顺序不同，结果不同

#### f-字符串

寻找花括号的变量名并替换，f 是formatting的简写

3.6 之后才有，f去寻找花括号的变量的值，可以解决数字不能与字符串相连的

~~~py
name = 'Burt'
f"What your {name}?"
~~~

不需要拼接用的加号和引号

以下交互模式

~~~python
>>> import math
>>> f"PI is about{math.pi:0.6}"
'PI is about3.14159'
>>> 6代表总共六位数的精度
~~~

#### 字符串和数字转换

int() 和float()

~~~python
 n = int(input("Please enter a number: "))
~~~

字符串不能进行加法运算 TypeError 错误

~~~python
>>> n =7
>>> print('hello'+n)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

~~~

3个数求和

~~~python
def inputnumbers():
    arry={}
    total = 0
    for n in range(3):
       #arry[n] = int(input(f"input the No.{n} number: \n"))
       total += int(input(f"input the No.{n+1} number: \n"))
    
    print(total)
inputnumbers()
'''
n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)
print(f"{n1} + {n2} + {n3} = {sum}")
'''
~~~





### 比较和排序

 `==`、`<` 和 `>` 等比较运算符在字符串上的效果和数字一样 

 字符串可以根据它们所含的字符排序。顺序和字母表顺序相似，但是并不完全一样： 

 你可以使用 `ord` 函数查询每个字符的数字值 

~~~python
print( ord('N')) #78
print( ord('A')) #65
print( ord('a')) #97
~~~

 `'A'` 开头的字符串将 `<` 任何以小写的 `'a'` 开头的字符串 



### starts_with

~~~python
# Add your function definition here
def starts_with(s1, s2):
    return (s1[0] == s2[0])
# A call like this should return True:
print(starts_with("banana", "bread"))

# And one like this should return False:
print(starts_with("zebonkey", "kiwi"))

'''
def starts_with(s1, s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False
'''
~~~

第二版

~~~python
# Write your function definition here.
def starts_with(long,short):
    for n in range(len(short)):
        return(long[n] == short[n])
# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))
'''
def starts_with(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True
'''
~~~

第三版

~~~python
# Write your function definition here.
def starts_with(long,short):
    return(long[:len(short)]==short)
# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))
~~~

第一个使用字符串索引操作，因此，当`position`变得大于`short`的长度时，会产生`IndexError`。另外两个使用切片，不产生`IndexError`。



### 字符串和数字互换

字符串和数字无法用+号直接拼接

int() 转化成整数，正数/负数/0

float() 转化成浮点数 float('56.234')

如果转化非数字字符串，回返回错误 ValueError



数字转字符串使用 str()

交互模式，拼接时间

~~~python
>>> hours = 21
>>> minutes = 16
>>> str(hours)+':'+str(minutes)
'21:16'
>>> f'Now is {hours} : {minutes}'
'Now is 21 : 16'
>>>
~~~



循环种累加

~~~python
for i in [1,2,3]:
		x = input('type the No.'+str(i)+' number(int/float) : ')
		t += float(x)
~~~

#### 字符串方法

判断语句，一般可以简写成

~~~python
return long[:len(short)] == short
~~~

不需要复杂的 return True /return False

**自带的有比较的函数 endswith / startswith** 

~~~python
>>> "banana".startswith("ban")
True
>>> "bonobo".startswith("ban")
False
~~~

HTML 标签判断

~~~python
def possible_tag(word):
    if word.startswith("<") and word.endswith("/>"):
        print(word,"could maybe be an HTML tag.")
    else:
        print(word,"is definitely not an HTML tag(but might contain one)")
        
possible_tag("<a apple />")
~~~

[官方String Methods档案]( https://docs.python.org/3/library/stdtypes.html#string-methods )

摘录

 `find`(*sub*[, *start*[, *end*]]) 

~~~python
>>> 'Py' in 'Python'
True
~~~

 `format`(**args*, ***kwargs*)  和f一样

~~~python
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
~~~

### 布尔值

True False

布尔运算有: and  or  not

![](.\screenshots\true_false-and_or.png)



 将其他值当做布尔值 

- 对于数字，零值被视为 false，所有非零值都被视为 true。
- 对于字符串，空字符串被视为 false，所有非空字符串都被视为 true。
- 对于列表，空列表被视为 false，所有非空列表都被视为 true。

### 课程10.列表 [ ]和字符串

 在 Python 中，列表和字符串具有一些共同点。它们都是**序列类型** — 它们表示一系列值，而不是单个值 

 **索引**操作、**切片**操作和 **`len` 函数**。因为它们都适用于序列，因此也适用于列表： 

len函数

~~~python
# Add your code here.
def total_length(list):
    total =0
    for n in list:
        total += len(n)
    return(total)
        
# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
print(total_length(["", '', "", '']))

'''
def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total
'''
~~~



#### 列表方法

~~~python
words = ["echidna", "dingo", "crocodile", "bunyip"]
~~~

1. append 

   `append` 方法会将项目添加到列表的末尾 

   ~~~python
   words.append("platypus")
   ~~~

   改变但是，不会有返回值

2. extend 

   会把字符串当成是 由单个字符组成的列表

   ~~~python
   words.extend("abc")
   ~~~

   传递的是字符串时，在words的结尾添加上，, 'a', 'b', 'c'

   ~~~python
   words.extend(["kangaroo", "wallaby"])
   ~~~

   则会在末尾添加 "kangaroo", "wallaby"。 当你将列表传递给 `words.extend` 时，它将该列表中的项目添加到 `words` 中。 

   append 是看做一个整体添加，哪怕是一个list，整体最为一个新的元素，添加到被添加的list

   ​	将其参数作为**单个项目**添加到列表的末尾。它只会在列表中添加**一个项**。

   extend会先拆开，字符串或者是list，然后一个一个的添加到末尾

   ​	将其参数视为一个序列，并**将序列中的每个项目添加到列表的末尾**。换句话说，它将项目的**序列**添加到列表中。

3. reverse

   ~~~python
   words.reverse()
   ~~~

   

   `reverse` 方法颠倒了列表的顺序。 

4. sort

   排序

    `sort` 方法会修改列表，使其按顺序排列 

以上4种方法都适用并修改列表，但是不返回任何值。

#### 可变性和共享结构

字符串和列表有很多相似的操作，但是**列表可以被修改，字符串则不行**。

列表可以用append 或者extend 来添加元素；

或者list[0] = new_value 来修改；

用sort来整理顺序

#### mutable 可以改变性（list） / immutable 不可改变性（string就是）

~~~python
>>> bunch = ['banana', 'banana', 'banana']
>>> bunches = [bunch, bunch, bunch]
>>> for b in bunches:
...     print(b)
['banana', 'banana', 'banana']
['banana', 'banana', 'banana']
['banana', 'banana', 'banana']
~~~



 列表 `[bunch, bunch, bunch]` 包含同一列表的三个引用。 

### 增量赋值

~~~python
x = x + 1
#可以缩写成
x += 1
~~~

 `x = x + 1` 和 `x += 1` 的结果完全一样。后者称为**增量赋值**语句。 

 如果有一个叫做 `toobig` 的变量，你希望用其值除以 2 

~~~python
toobig /= 2
~~~

### 遍历字符串和列表

~~~python
for x in "many words":
    print(x)
~~~



### While循环

会在符合判断语句，如果满足一直重复

~~~python
def password_check():
    while input("Type your PassWord :") != 'BadPwd':
        print("Wrong,try again")
    print("Greattings!")
password_check()
~~~

while 和if 不同，可以运行多次。

~~~python
def count_ch(string,traget):
    index = 0
    total =0
    while index < len(string):
        if string[index:index+len(traget)] == target:
            total += 1
        index += 1
    print(target,"show ",total," times in",string)
count_ch("oxen and foxen all live in boxen","l")
~~~

~~~python
import time
n = 10
while n > 0:
    print(n)
    time.sleep(1)	#暂停一秒再进入下一个循环
    n -= 1
print("Blastoff!")
~~~

#### for循环和while循环

1. for 要针对一个变量，比如 for n in rang()
2. for 会循环全部范围，一般使用if判断语句去提前中断
3. while 要为循环使用变量，则必须使用`index = 0`行创建一个变量，然后在循环中去处理
4. `for`循环到达序列末尾（如列表末尾）会自动停止，但是while循环只有在其条件满足时才停止

### 无限循环

~~~python
while True:
    print('Help! trapped in an infinite loop')
~~~

使用CTRL+c来中止循环输出。

#### break 语句

还有一种退出无限循环的方式。在 `while` 或 `for` 循环里，你可以使用 `break` 语句立即退出循环

~~~python
def no_repeating():
    word = []
    while True:
        word = input('Input a word')
        if word in words:
            print('You type this word already!')
            break
        words.append(word)
    return words

no_repeating()
~~~



习题

~~~python
>>> def find_512():
...     for x in range(100):
...         for y in range(100):
...             if x*y ==512:
...                 return f'{x}*{y} ==512'

>>> find_512()
'8*64 ==512'
~~~

### 查找子字符串 

substring search 子字符串搜索

~~~python
def is_substring(short, long):
    index = 0
    while index < (len(long) - len(short) + 1):
        if long[index : index + len(short)] == short:
            return True
        index += 1
    return False
~~~

### 10-15 更多字符串方法：

1. in 查找是否存在 子字符串，对于list是否是一个元素

   ~~~python
   >>> [2,3] in [1,2,3,4,]
   False
   >>> [2,3] in [1,[2,3],4,]
   True
   #所以list本身不in 本身
   >>> [1,2,3,4] in [1,2,3,4]
   False
   ~~~

2. not in 与in 相反

3. find 找出sub字段，返回indx值，不存在的话返回-1

   ~~~python
   >>> a=[1,2,3,4]
   >>> b=[2,3]
   a.find(b)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'list' object has no attribute 'find'
   ~~~

4. count 返回不重叠的次数，处理list时，与in一致，也是元素匹配，不是简单值的符合

   ~~~python
   >>> a=[1,2,3,4]
   >>> b=[2,3]
   >>> a.count(b)
   0
   >>> c=[1]
   >>> a.count(c)
   0
   >>> d=1
   >>> a.count(d)
   1
   ~~~

练习：

在双城记中寻找巧克力

1. 单词 "chocolate" 在小说里出现了多少次？

   tale.count("chocolate")

2. 是 或 否：单词 "chocolate" 是否出现在了小说里？

   "chocolate" in tale

3. 单词 "chocolate" 第一次在小说里的哪处出现？

   tale.find("chocolate")

### 10-16 Join方法

~~~python
"-".join("cat")
'c-a-t'
~~~

~~~python
def breakify(str):
    return (' <br> '.join(str))

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
print(breakify(lines))
~~~

### 10-17 修改字符串

要明确一点，字符串是无法直接修改的。只能迂回的方法

~~~python
string = "Hello world!"
print(string.split(' '))
output = [] # Create empty list
index = 0
while index < len(string):
    output.append(string[index]) # Append current character
    index += 1 # Move on to next character

print(output)
>>>
['Hello', 'world!']
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
~~~

【待更新】用for循环没有改写成功

##  11 管理文件

### 11-1.文件

文件在删除前持久存储在硬盘，可以被多个程序调用

### 11-2 ~3 整理照片

任务：具有地点名称的照片，进行文件夹整理

![image-20200324165131502](README.assets/image-20200324165131502.png)

ls在python中不可用，python有自有的函数

### 11-4 ~5 OS模块

1. os.mkdir 创建新的文件夹
2. os.rename  移动文件到另外一个文件夹
3. os.listdir 列出文件夹文件

使用前记得一定要导入，而且函数前要冠名

~~~python
import os
os.listdir()
os.mkdir('new_dir')
os.rename('some.txt','new_dir/some.txt')
~~~

### 11-6 相对路径和当前工作目录

1. os.getcwd() 当前工作目录
2. os.chdir() 更换目录

PHP也是这两个函数

使用os.rename()改变目录时，需要匹配对目录。比如，需要前换到对应的目录为当前工作目录

### 11-7 os 函数和 shell 命令

1. python中的 os.getcwd() 和shell的pwd相似，而且os.getcwd()可以传递给参数

2. os.listdir()  与 ls 命令

3. os.mkdir() 与 mkdir 命令

4. os.rename() 与 mv 命令 移动或修改 文件或 文件夹的名

   ~~~python
   os.rename(src , dst)
   src 参数用于指定要进行重命名的目录或文件；dst 参数用于指定重命名后的目录或文件。
   ~~~

   

5. os.chdir() 与 cd 命令

6. win 系统文件path 用的是反斜杠 \ ,linux是斜杠 /

7. os.path.join('Downloads','amazing_thing.py') 会总转换 win/ linux系统的文件夹连接符,注意os.pth.join(路径，文件名)

### 11-8 拆分文件名

`split` 操作根据你所选的字符拆分字符串，在此示例中是空格！

~~~python
str.split(" ")
~~~

~~~python
def extract_place(fname):
    return fname.split('_')[1]
~~~



练习：

sentence = "I need a banana split!"

sentence.split(" ")

["I", "need", "a", "banana", "split!"]

### 11-9 创建文件夹

~~~python
def make_place_directories(places):
    for place in places:
        os.mkdir(place)
make_place_directories('beijing','shanghai')
~~~

注意，不可出现重复文件夹，会中止创建剩下的

### 11-10 整理照片

~~~python
def organize_photos(directory):
    #从文件中获取所有地点名称
    ##第一确保切换到了指定目录
    os.chdir(directory)
    places =[]
    all_files = os.listdir()
    for fname in all_files:
        if extract_place(fname) not in places:
            places.append(extract_place(fname))
    #创建各个地点文件夹
    make_place_directories(places)
        
    #os.rename() 整理到对应的文件夹
    for fname in all_files:
        os.rename(fname,os.path.join(extract_place(fname),fname))
~~~

### 11-11 脚本标注

运行python的不同方式包括：

* 命令行
* import导入在另外一个文件使用

在使用import 导入模块时，python会运行此模块所有代码

Dunder变量

~~~python
if __name__ == '__main__':
    xxxxx
    organize_photos("C:/Users/Admin/Desktop/photos")
~~~

**如果模块是被直接运行的，则xxx代码块被运行，如果模块是被导入的，则xxx代码块不被运行**。这样别人引用的时候，就不会改变别人的photos的文件夹下内容

> 有时我们写了可以直接被执行的模块（.py文件），但是在另一个程序中调用它时，我们其实只是想用一用里面写好的函数，而不是全都执行一遍。那么我们就可以把执行的部分放到if __name__ == '__main__' 中进行判断。
>
> 如果if __name__ == '__main__' 为真，就说明我们是在直接执行这个模块，那么所有的操作都要运行一遍；但如果为假，就说明我们是引用了这个模块，只有在需要用到它的函数时，才会被调用执行。
>
> 
>
> 作者：师师
> 链接：https://www.zhihu.com/question/49136398/answer/613131588
> 来源：知乎
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

在命令行中为if将会执行此代码

如果是import导入到别的程序，if的判断值为false，函数将不会被调用

### 11-12 pycodestyle

~~~python
C:\Users\Admin>pip install pycodestyle
Collecting pycodestyle
  Downloading https://files.pythonhosted.org/packages/0e/0c/04a353e104d2f324f8ee5f4b32012618c1c86dd79e52a433b64fceed511b/pycodestyle-2.5.0-py2.py3-none-any.whl (51kB)
     |████████████████████████████████| 51kB 363kB/s
Installing collected packages: pycodestyle
Successfully installed pycodestyle-2.5.0
~~~

~~~python
D:\Online\Udacity\udacity-python-28-days> pycodestyle 11-10_organize_photos.py
11-10_organize_photos.py:2:1: E302 expected 2 blank lines, found 0
11-10_organize_photos.py:4:1: E302 expected 2 blank lines, found 0
11-10_organize_photos.py:6:1: E302 expected 2 blank lines, found 0
11-10_organize_photos.py:10:1: E302 expected 2 blank lines, found 1
11-10_organize_photos.py:13:13: E225 missing whitespace around operator
11-10_organize_photos.py:23:24: E231 missing whitespace after ','
11-10_organize_photos.py:23:43: E231 missing whitespace after ','
11-10_organize_photos.py:24:9: E265 block comment should start with '# '
11-10_organize_photos.py:25:1: E302 expected 2 blank lines, found 0
11-10_organize_photos.py:28:13: E225 missing whitespace around operator
11-10_organize_photos.py:31:80: E501 line too long (89 > 79 characters)
11-10_organize_photos.py:34:5: E265 block comment should start with '# '
11-10_organize_photos.py:38:31: E225 missing whitespace around operator
11-10_organize_photos.py:42:28: E231 missing whitespace after ','
11-10_organize_photos.py:42:47: E231 missing whitespace after ','
11-10_organize_photos.py:43:13: E265 block comment should start with '# '
11-10_organize_photos.py:44:1: E265 block comment should start with '# '
11-10_organize_photos.py:45:1: E305 expected 2 blank lines after class or function definition, found 0
11-10_organize_photos.py:45:46: W292 no newline at end of file
~~~

保存后可以继续验证，没有消息就是好消息

练习

~~~python
$ pycodestyle spin.py
spin.py:5:20: E201 whitespace after '('
spin.py:5:24: E202 whitespace before ')'
spin.py:13:3: E111 indentation is not a multiple of four

~~~

### 11-13 _14 脏话过滤器

过滤的文件内的一段文字，不是文件名

解决方案，将内容split成字符，然后匹配。而不是，一个一个的字符去循环匹配。

#### 13-15_16 打开并读取文件 关闭文件

~~~python
my_story = open("admin/my_story.txt")
contents = my.story.read() 
contents #将输出内容字符串
~~~



~~~python
my.story.close()
~~~

关闭后就不可以再打开。

使用with 语句读取后，自动关闭

~~~python
with open(my_story.py) as my_story:
    print(my_story)

~~~

测试系统最多可以打开多少文件

~~~python
>>> import os
>>> os.getcwd()
'D:\\Online\\Udacity\\udacity-python-28-days'
>>> count =0
>>> files =[]
>>> while True:
...     count +=1
...     print(f"opening files # {count}")
...     files.append(open("somefile.txt"))
...
opening files # 8190
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
OSError: [Errno 24] Too many open files: 'somefile.txt'
~~~

练习：

~~~python
>>> with open(read.txt) as getread:
...     print(getread)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'txt'
~~~

上面报错，文件名缺少了引号

~~~python
>>> with open('read.txt') as read:
...     print(read)
... 
<_io.TextIOWrapper name='read.txt' mode='r' encoding='UTF-8'>
~~~

上面报错，因为line 2 没有read()方法，如果还不对，可以参考下面

~~~python
>>> with open('read.txt','r',encoding='UTF-8') as read:
...     print(read.read())
... 
Reading files is cool, but don't forget to close them when you're done!
~~~



正确答案：

~~~python
>>> with open('read.txt') as read:
...     print(read.read())
... 
Reading files is cool, but don't forget to close them when you're done!

>>> 
~~~

#### 13-17 低效率方案

~~~python
rude_words =["crap","darn"]

#os.chdir(dir)
with open('my_story.txt') as myfile:
    contents = myfile.read()
    rude_count = 0
    for rude in rude_words:
        if rude in contents:
            rude_count +=1
            print(f"Found rude word : {rude}")
if rude_count ==0:
    print("No rude words")
~~~

问题点：每一个单词都要和全文进行一次匹配。

优点：比纯英文的split 空格分开来说，可以查找到没有被空格分开的关键字

#### 13-18 一次读取一个单词

思路把内容split后保存到内存

~~~python
rude_words =["crap","darn"]

#os.chdir(dir)
with open('my_story.txt') as myfile:
    contents = myfile.read()
    rude_count = 0
    content_words = contents.split(" ")
    for word in content_words:
        if word in rude_words:
            rude_count +=1
            print(f"Found rude word : {word}")
if rude_count ==0:
    print("No rude words")
~~~

这样修改，全文就只读取一遍，全文的每个单词会跟检查list进行检查。

为了避免过大文件直接载入内存，可以一行一行的读取内容。使用for来读取就是一行一行的方式

~~~python
rude_words =["crap","darn"]

#os.chdir(dir)
with open('my_story.txt') as myfile:
    rude_count =0
    for line in myfile:
        content_words = contents.split(" ")
        for word in content_words:
            if word in rude_words:
                rude_count +=1
                print(f"Found rude word : {word}")
if rude_count ==0:
    print("No rude words")
~~~

然后，def 函数封装

~~~python
rude_words =["crap","darn"]
def check_line(line):
    rude_count=0
    content_words = line.split(" ")
        for word in content_words:
            if word in rude_words:
                rude_count +=1
                print(f"Found rude word : {word}")
        return rude_count
def check_file(filename):
	with open(filename) as myfile:
        count =0
        for line in myfile:
            count += check_line(line)
        if count ==0:
            print("No rude words")
        
if __name__ == "__main__":
    check_file("my_story.txt")
~~~

#### 13-19 标点符号

因为英文标点符号和单词想是相连的。split 空格分开后会遗漏。

~~~python
import string    #注意使用前要先将string模块导入
 
>>> s="We met at the wrong time, but separated at the right time. The most urgen
t is to take the most beautiful scenery!!! the deepest wound was the most real e
motions."
>>> for i in s:
...     if i in string.punctuation:  #如果字符是标点符号的话就将其替换为空格
...         s = s.replace(i," ")
...
>>> s
'We met at the wrong time  but separated at the right time  The most urgent is t
o take the most beautiful scenery    the deepest wound was the most real emotion

~~~

来自：[CSDN](https://blog.csdn.net/kongsuhongbaby/article/details/83181768)



练习：

如果你针对字符串向 `strip` 函数传递 `string.punctuation`，该字符串里的所有标点将被删除

~~~python
import string
rude_words =["crap","darn"]
def check_line(line):
    rude_count=0
    content_words = line.split(" ")
        for word in content_words:
            if word in rude_words:
                rude_count +=1
                print(f"Found rude word : {word}")
        return rude_count
def check_file(filename):
	with open(filename) as myfile:
        
        count =0
        for line in myfile:
            count += check_line(line)
        if count ==0:
            print("No rude words")
        
if __name__ == "__main__":
    check_file("my_story.txt")
~~~

strip 是去除首位匹配的字符：

~~~
 str = "00000003210Runoob01230000000";
>>> print (str.strip( '0' )) # 去除首尾字符 0
3210Runoob0123 
~~~



`string.punctuation` 就一个包含了各种符号的参数

~~~
import string
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
~~~

所以修改后：

~~~python
import string
rude_words = ["crap", "darn"]


def check_line(line):
    rude_count = 0
    content_words = line.split(" ")
    for word in content_words:
        word = word.strip(string.punctuation)
        if word in rude_words:
            rude_count += 1
            print(f"Found rude word : {word}")
    return rude_count


def check_file(filename):
    with open(filename) as myfile:
        count = 0
        for line in myfile:
            count += check_line(line)
        if count == 0:
            print("No rude words")

if __name__ == "__main__":
    check_file("my_story.txt")
~~~

#### 11-20 首字母大写的匹配

lower()函数全部转为小写，此外还有

* upper()全部转为大写

  ~~~python
  str ='Ok Nice to Meet you'
  str.upper()
  'OK NICE TO MEET YOU'
  ~~~

* swapcase() 方法用于对字符串的大小写字母进行转换

  ~~~python
  str ='Ok Nice to Meet you'
  str.swapcase()
  'oK nICE TO mEET YOU'
  ~~~

* title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始

  ~~~python
  str ='Ok Nice to Meet you'
  str.title()
  'Ok Nice To Meet You'
  ~~~

* count 计数

  ~~~python
  str ='Ok Nice to Meet you'
  str.count('o')
  2
  ~~~

  修改后

  ~~~python
  import string
  rude_words = ["crap", "darn"]
  
  
  def check_line(line):
      rude_count = 0
      content_words = line.split(" ")
      for word in content_words:
          word = word.strip(string.punctuation)
          if word.lower() in rude_words:
              rude_count += 1
              print(f"Found rude word : {word}")
      return rude_count
  
  
  def check_file(filename):
      with open(filename) as myfile:
          count = 0
          for line in myfile:
              count += check_line(line)
          if count == 0:
              print("No rude words")
  
  if __name__ == "__main__":
      check_file("my_story.txt")
  ~~~

### 11-21 写入文件



练习

~~~python
>>> with open("newfile.txt","w") as newf:
...     i = 0
...     while i< 31 :
...         newf.write(f"{i}")
...         i +=1
... 

>>> with open("newfile.txt") as newf:
...     for line in newf:
...         print(line)
... 
0123456789101112131415161718192021222324252627282930

>>> os.listdir()
['newfile.txt', 'read.txt', '2nd-new.txt']

>>>with open("read.txt") as orig:
...     with open("2nd-new.txt","w") as cop:
...         for line in orig:
...             cop.write(f"{line}")
... 
72
>>> with open("2nd-new.txt") as file2:
...     for line in file2:
...         print(line)
... 
Reading files is cool, but don't forget to close them when you're done!
~~~

答案：

~~~python
with open("numbers.txt", "w") as writer:
    # Write even numbers from 0 to 30
    for num in range(0, 31):
        if num % 2 == 0:
            writer.write(f"{num}\n")

# Copy contents of one file to another
with open("read.txt") as reader:
    with open("copy.txt") as copy:
        copy.write(reader.read())
~~~

上述代码：

* 如果不存在read.txt程序崩溃
* 如果 read.txt 太大，放不进内存，崩溃

待做：

将rude词语换成***，replace 函数，读取再写入

## 12 网络API

### 12-1 API **应用编程接口**

有点类似调用模块里的函数，只是远程帮我们计算处理。API 是一个接口。创建它的目的是帮助两个不同的应用交互。

### 12-2 获取天气数据

~~~python
https://www.metaweather.com/api/location/search/?query=
~~~

浏览器会将空格替换为专门表示空格的特定代码 `%20`

~~~shell
curl https://www.metaweather.com/api/location/search/?query=New%20Delhi
[{"title":"New Delhi","location_type":"City","woeid":28743736,"latt_long":"28.643999,77.091003"}]
~~~

练习：

~~~shell
curl https://www.metaweather.com/api/location/28743736/

{"consolidated_weather":[{"id":4729749567963136,"weather_state_name":"Light Cloud","weather_state_abbr":"lc","wind_direction_compass":"NW","created":"2020-03-31T00:25:43.601239Z","applicable_date":"2020-03-31","min_temp":18.81,"max_temp":33.81,"the_temp":31.06,"wind_speed":5.768218554282988,"wind_direction":308.46148742094334,"air_pressure":1012.0,"humidity":31,"visibility":13.669234172432992,"predictability":70},{"id":5149635637149696,"weather_state_name":"Light Cloud","weather_state_abbr":"lc","wind_direction_compass":"NW","created":"2020-03-31T00:25:46.472301Z","applicable_date":"2020-04-01","min_temp":19.96,"max_temp":34.525000000000006,"the_temp":32.225,"wind_speed":5.029699959243352,"wind_direction":318.99347765905793,"air_pressure":1011.0,"humidity":30,"visibility":12.578417044460352,"predictability":70},{"id":5244641588805632,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"WNW","created":"2020-03-31T00:25:49.473227Z","applicable_date":"2020-04-02","min_temp":20.335,"max_temp":34.215,"the_temp":31.935,"wind_speed":5.4370671315782495,"wind_direction":300.10561620978945,"air_pressure":1011.0,"humidity":27,"visibility":12.533678318619263,"predictability":68},{"id":6299971793977344,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"NW","created":"2020-03-31T00:25:52.575922Z","applicable_date":"2020-04-03","min_temp":20.674999999999997,"max_temp":34.834999999999994,"the_temp":32.44,"wind_speed":5.968544966945042,"wind_direction":311.00918115961116,"air_pressure":1011.0,"humidity":22,"visibility":12.621602342320845,"predictability":68},{"id":6275577990348800,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"WNW","created":"2020-03-31T00:25:55.584865Z","applicable_date":"2020-04-04","min_temp":21.01,"max_temp":36.120000000000005,"the_temp":32.86,"wind_speed":5.626865080407751,"wind_direction":303.17550226801234,"air_pressure":1011.5,"humidity":19,"visibility":12.66012735623956,"predictability":68},{"id":6048661681209344,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"NW","created":"2020-03-31T00:25:58.485356Z","applicable_date":"2020-04-05","min_temp":21.545,"max_temp":37.605000000000004,"the_temp":35.51,"wind_speed":5.160611429253162,"wind_direction":309.0,"air_pressure":1008.0,"humidity":14,"visibility":9.999726596675416,"predictability":68}],"time":"2020-03-31T07:49:59.523844+05:30","sun_rise":"2020-03-31T06:12:39.802406+05:30","sun_set":"2020-03-31T18:39:14.473371+05:30","timezone_name":"LMT","parent":{"title":"India","location_type":"Country","woeid":23424848,"latt_long":"21.786600,82.794762"},"sources":[{"title":"BBC","slug":"bbc","url":"http://www.bbc.co.uk/weather/","crawl_rate":360},{"title":"Forecast.io","slug":"forecast-io","url":"http://forecast.io/","crawl_rate":480},{"title":"Met Office","slug":"met-office","url":"http://www.metoffice.gov.uk/","crawl_rate":180},{"title":"OpenWeatherMap","slug":"openweathermap","url":"http://openweathermap.org/","crawl_rate":360},{"title":"World Weather Online","slug":"world-weather-online","url":"http://www.worldweatheronline.com/","crawl_rate":360}],"title":"New Delhi","location_type":"City","woeid":28743736,"latt_long":"28.643999,77.091003","timezone":"Asia/Kolkata"}
~~~

### 12-3 requests 模块

~~~python
pip install requests
#or
pip3 install requests
~~~

~~~shell
PS C:\Windows\system32> pip install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 393kB/s
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/b9/63/df50cac98ea0d5b006c55a399c3bf1db9da7b5a24de7890bc9cfd5dd9e99/certifi-2019.11.28-py2.py3-none-any.whl (156kB)
     |████████████████████████████████| 163kB 939kB/s
Collecting idna<3,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 1.3MB/s
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/e8/74/6e4f91745020f967d09332bb2b8b9b10090957334692eb88ea4afe91b77f/urllib3-1.25.8-py2.py3-none-any.whl (125kB)
     |████████████████████████████████| 133kB 312kB/s
Collecting chardet<4,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
     |████████████████████████████████| 143kB 726kB/s
Installing collected packages: certifi, idna, urllib3, chardet, requests
Successfully installed certifi-2019.11.28 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.8
~~~



使用requests

~~~python
import requests
r = requests.get('https://api.github.com/events')
r
<Response [200]>
~~~

### 12-4 发出请求

requests.get('https://xxxxx') 网址部分需要添加https://或者http://

不然

~~~
requests.exceptions.MissingSchema: Invalid URL 'https//github.com': No schema supplied. Perhaps you meant http://https//github.com?
~~~



~~~python
r = requests.get('https://github.com')
>>> r
<Response [200]>
>>> r.status_code
200
>>> r.text
~~~

练习

~~~python
>>> import requests
>>> r = requests.get('http://localhost:9999/secret')
>>> r
<Response [200]>
>>> r.text
'mango'
>>> 
~~~

### 12-5 debug

* 网络具有不确定性 Non-deterministic
* 需要考虑网络不稳定因素带来的错误

练习

~~~python
import requests
r = requests.get('https://www.google.com/monkeybagel/')
print(type(r.status_code))
if r.status_code == 404:
    print('Page not find')
~~~

### 12-6 Try 和Exceptions

异常： NameError 、ZeroDivisionError 、OSError

异常和错误的区别：要求作出一个八边形，却画出六边形，这是一个错误，却没有反馈异常。

try ... except ：

* 类似if 语句
* try ... except 语句只能捕获当前复合语句内的错误，语句外的错误还是会报错返回traceback
* 无法捕获语法错误，SytaxError ，因为语法错误在运行代码前就发生了

requests 的一个错误是

~~~~python
requests.exceptions.ConnectionError
~~~~

~~~python
import requests
try:
    r = requests.get('https://sqdmqpoijdqnfcowinfvow.com')
    print(r.text)
except requests.exceptions.ConnectionError:
    print('Could not connect')
~~~

练习：

python在 运行代码时（不是之前，也不是之后）会抛出错误

~~~python
try:
    print(17 / 0)
except IndexError:
    print("negative forty-two")
~~~

如果except标注的不对，也会输出traceback

~~~python
def takeoff():
    print(TAKEOFF)

try:
    print("3, 2, 1, ...")
    takeoff()
except NameError:
    print("Failed to launch")
~~~

> 输出 `3, 2, 1, ...` 的语句将运行，然后 `takeoff` 函数被调用。但是，名称 `TAKEOFF` 未定义，因此 `takeoff` 函数将导致 `NameError`。`try ... except` 语句捕获该异常并输出 `Failed to launch`。

练习

~~~python
import requests
try:
    r = requests.get("https://www.udacity.com")
    print(r.status_code)
except requests.exceptions.ConnectionError:
    print("can not connect.")

~~~

答案

~~~python
import requests

try:
    r = requests.get("https://www.udacity.com")
    print(r) # If you did print(r.status_code), that also works!
except requests.exceptions.ConnectionError:
    print("Could not connect to server.")
~~~

### 12-7 JSON

JSON 是一种格式，它是一种构建数据的方式，让用不同语言（包括 Python）编写的代码能够轻松地利用这种数据。

### 12-8 ~ 9 字典

1. 创建

   ~~~python
   d ={}
   ~~~

2. key-value 键值对作为item。key唯一

3. 查询

   ~~~python
   >>> d ={}
   >>> d['color'] = 'red'
   >>> d['size'] = 'small'
   >>> d
   {'color': 'red', 'size': 'small'}
   >>> d[1]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 1
   >>> d['color']
   'red'
   >>>>>> d['size'] += 'small-01'#追加
   >>> d['size']
   'smallsmall-01'
   
   >>> d['name']='Peter'
   >>> d['name']
   'Peter'
   >>> d['name']='JACK'
   >>> d['name']
   'JACK'
   ~~~

练习：

~~~python
d = {'bird': 'tweet', 'fish': 'splash'}
d['wolf'] = 'bark'
print(d['fish'][1] + d['wolf'][1:])
park
~~~

~~~python
>>> d ={}
>>> d['e']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'e'
~~~

尝试在字典里访问不存在的键将生成 `KeyError`。list才是index

* `in` 操作符用来判断 `x` 是否是字典 `d` 里的键！

* 列表是可变的，而字符串是不可变的，字典是可变的 mutable

* `del` 语句会**删除**字典里的条目。

  ~~~python
  d = {'fish': 'salmon', 'cat': 'lion'}
  del d['fish']
  print(d)
  ~~~

12-11 遍历字典

~~~python
favorites = {'color': 'purple', 'number': 42, 'animal': 'turtle', 'language': 'python'}
for item in favorites:
    print(item)

color
number
animal
language
~~~

如果我们只是遍历字典，Python 的默认行为是遍历字典里的键

* 获取字典的键值

  ~~~python
  for key in favorites.keys():
      print(key)
  ~~~

也是返回key，是不指定的情况下默认行为

* 获取字典的值

  ~~~python
  for value in favorites.values():
  ~~~

* 获取 完整的键值对 

  ~~~python
  for entry in favorites.items():
     print(entry)
  
  ('color', 'purple')
  ('number', 42)
  ('animal', 'turtle')
  ('language', 'python')
  ~~~

  注意，代码以键值对的形式输出了每个条目，并且用逗号分隔

  ~~~python
  for key, value in favorites.items():
      print(key)
      print(value)
  ~~~

~~~python
for key, value in favorite.items():
    print(f"my favorite {key} is {value}")
~~~

#### 元组

代码 `('color', 'purple')` 看起来像个列表，但是有小括号 `( )`，而不是方括号 `[ ]`。

这是一种数据结构类型，叫做**元组**。

* 元组属于序列，和列表一样。

* 但是它们不可变，对于列表，创建好列表后可以更改列表里的值。对于元组则不行。

练习

~~~python
str = 'it appears that the the appears the most in the sentence'
dict = {}
list = str.split(" ")
for n in list:
    dict[n] =str.count(n)
for key,value in dict.items():
    #print(f"{key} show in str {value} times")
    print(f"\'{key}\' appears {value} time(s) in the string")

~~~

答案

~~~python
str = 'it appears that the the appears the most in the sentence'
dict = {}
list = str.split(" ")
for word in list:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
for key, value in dict.items():
    print(f"\'{key}\' appears {value} time(s) in the string")
~~~

### 12-15-18 嵌套数据结构

字典的键的类型

> **列表**不能用作键。如果你尝试了，应该会遇到以下 traceback：`TypeError: unhashable type: 'list'`。
>
> **字典**不能用作键。如果你尝试了，应该会遇到以下 traceback：`TypeError: unhashable type: 'list'`。

如果你使用列表作为字典的键，然后修改了列表，这样就不确定你希望键是列表的旧值还是新值！

字典值的类型，所有类型都可以。

~~~python
d = {'a': [{'b': 'c'}, {'d': 'e'}], 'f': 'g'}
>>>d['a']
[{'b': 'c'}, {'d': 'e'}]
>>>d['a'][1]
{'d': 'e'}
>>>d['a'][1]['d']
'e'
>>>d['a'][0]['b']
'c'
~~~



~~~python
代码 d['a'][0]['b'] 的作用是将索引操作符相连，深入挖掘数据的嵌套结构，每个索引操作符都深入一个级别。
~~~

* 列表里可以有字典元素

  ~~~python
  l = ['a', {'b': 'c', 'd': 'e'}]
  ~~~

* 字典里可以有列表元素

  ~~~~python
  d = {'a': [{'b': 'c'}, {'d': 'e'}]}
  ~~~~

循环 字典里的字典元素

~~~python
pets = {
    'birds': {
        'parrot': 'Arthur',
        'canary': 'Ford'
    },
    'fish': {
        'goldfish': 'Zaphod',
        'koi': 'Trillium'
    }
}

for e in pets:
    print(e)
    #print(type(pets[e]))
    #print(pets[e])
    for key,value in pets[e].items():
        print(f"{key},{value}")

        
        
birds
parrot,Arthur
canary,Ford
fish
goldfish,Zaphod
koi,Trillium
~~~

读取 字典组成的列表

~~~python
weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for e in weather:
    
    print(e)
    for key,value in e.items():
        print(f"{key},is {value}")

        
{'date': 'today', 'state': 'cloudy', 'temp': 68.5}
date,is today
state,is cloudy
temp,is 68.5
{'date': 'tomorrow', 'state': 'sunny', 'temp': 74.8}
date,is tomorrow
state,is sunny
temp,is 74.8
~~~

### 12-19 简单天气输出

~~~python
weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for forecast in weather:
    print(forecast['date'])
    print(forecast['state'])
    print(forecast['temp'])
    print(f"The weather for {forecast['date']} will be {forecast['state']} with a temperature of {forecast['temp']} degrees.")

>>>    
today
cloudy
68.5
The weather for today will be cloudy with a temperature of 68.5 degrees.
tomorrow
sunny
74.8
The weather for tomorrow will be sunny with a temperature of 74.8 degrees.
~~~

最优雅答案

~~~python
for forecast in weather:
    date = forecast['date']
    state = forecast['state']
    temp = forecast['temp']
    print(f"The weather for {date} will be {state} with a temperature of {temp} degrees.")
~~~

12-20 真实天气数据

1. 获取城市WOEID 

   ~~~
   https://www.metaweather.com/api/location/search/?query=beijing
   [{"title":"Beijing","location_type":"City","woeid":2151330,"latt_long":"39.906010,116.387909"}]
   [{"title":"Dongguan","location_type":"City","woeid":2161842,"latt_long":"23.046499,113.735817"}]
   ~~~

   

2. 获取城市数据

   ~~~~
   https://www.metaweather.com/api/location/2161842/
   
   >>>
   {"consolidated_weather":
   [{"id":6652007010009088,"weather_state_name":"Heavy Rain","weather_state_abbr":"hr","wind_direction_compass":"NNE","created":"2020-03-31T06:54:32.900118Z","applicable_date":"2020-03-31","min_temp":16.25,"max_temp":20.83,"the_temp":19.055,"wind_speed":4.153946038940587,"wind_direction":24.497022441861475,"air_pressure":1015.0,"humidity":88,"visibility":6.140079436093215,"predictability":77},
   {"id":4854044042461184,"weather_state_name":"Light Rain","weather_state_abbr":"lr","wind_direction_compass":"NNE","created":"2020-03-31T06:54:35.841360Z","applicable_date":"2020-04-01","min_temp":18.43,"max_temp":24.29,"the_temp":21.314999999999998,"wind_speed":4.22691525905777,"wind_direction":32.483974436990124,"air_pressure":1017.0,"humidity":83,"visibility":9.887258410880458,"predictability":75},
   {"id":5495773930192896,"weather_state_name":"Light Rain","weather_state_abbr":"lr","wind_direction_compass":"ESE","created":"2020-03-31T06:54:38.818207Z","applicable_date":"2020-04-02","min_temp":20.47,"max_temp":26.55,"the_temp":23.735,"wind_speed":5.79158378145497,"wind_direction":117.79904866816615,"air_pressure":1018.5,"humidity":75,"visibility":10.115612324027678,"predictability":75},{"id":5982180150870016,"weather_state_name":"Showers","weather_state_abbr":"s","wind_direction_compass":"ESE","created":"2020-03-31T06:54:42.023996Z","applicable_date":"2020-04-03","min_temp":20.6,"max_temp":27.095,"the_temp":24.064999999999998,"wind_speed":5.285056659304329,"wind_direction":116.83238443691666,"air_pressure":1018.5,"humidity":73,"visibility":10.39243319016941,"predictability":73},
   {"id":5419230197448704,"weather_state_name":"Light Rain","weather_state_abbr":"lr","wind_direction_compass":"E","created":"2020-03-31T06:54:44.897674Z","applicable_date":"2020-04-04","min_temp":21.055,"max_temp":27.325,"the_temp":23.659999999999997,"wind_speed":4.394960584042525,"wind_direction":91.60905974630204,"air_pressure":1019.0,"humidity":75,"visibility":8.223847729261115,"predictability":75},
   {"id":5528150836510720,"weather_state_name":"Heavy Rain","weather_state_abbr":"hr","wind_direction_compass":"E","created":"2020-03-31T06:54:47.746012Z","applicable_date":"2020-04-05","min_temp":19.195,"max_temp":23.61,"the_temp":23.93,"wind_speed":4.0868591426071745,"wind_direction":91.50000000000001,"air_pressure":1020.0,"humidity":74,"visibility":9.160875487155014,"predictability":77}],
   "time":"2020-03-31T16:12:32.440831+08:00","sun_rise":"2020-03-31T06:17:27.724956+08:00","sun_set":"2020-03-31T18:40:17.023721+08:00","timezone_name":"LMT",
   "parent":{"title":"China","location_type":"Country","woeid":23424781,"latt_long":"36.894451,104.165649"},"sources":[{"title":"Forecast.io","slug":"forecast-io","url":"http://forecast.io/","crawl_rate":480},{"title":"HAMweather","slug":"hamweather","url":"http://www.hamweather.com/","crawl_rate":360},{"title":"Met Office","slug":"met-office","url":"http://www.metoffice.gov.uk/","crawl_rate":180},{"title":"OpenWeatherMap","slug":"openweathermap","url":"http://openweathermap.org/","crawl_rate":360},{"title":"Weather Underground","slug":"wunderground","url":"https://www.wunderground.com/?apiref=fc30dc3cd224e19b","crawl_rate":720},{"title":"World Weather Online","slug":"world-weather-online","url":"http://www.worldweatheronline.com/","crawl_rate":360}],"title":"Dongguan","location_type":"City","woeid":2161842,"latt_long":"23.046499,113.735817","timezone":"Asia/Shanghai"}
   ~~~~

从 JSON 文本更改为 Python 字典

~~~python
d = r.json()
~~~

~~~python
import requests
r = requests.get('https://www.metaweather.com/api/location/2161842')
d = r.json()
#for item in d['consolidated_weather'].items():
#    print(item)
for item in d['consolidated_weather']:
    print(item)
    print(item['id'])
~~~



### 12-20~22 获取天气预报

~~~python
import requests
r = requests.get('https://www.metaweather.com/api/location/2161842')
d = r.json()
#for item in d['consolidated_weather'].items():
#    print(item)
for item in d['consolidated_weather']:
    #print(item)
    #print(item['applicable_date'])
    #print(item['humidity'])
    applicable_date =item['applicable_date']
    humidity =item['humidity']
    print(f"the humidity of {applicable_date} is {humidity}.")
~~~

答案

~~~python
import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()

for forecast in d['consolidated_weather']:
    date = forecast['applicable_date']
    humidity = forecast['humidity']
    print(f"{date}\tHumidity: {humidity}")
~~~

12-23 复习

1. ~~~python
   import requests
   yahoo = requests.get("https://www.yahoo.com/")
   print(yahoo.text)
   ~~~

   变量 `yahoo` 是什么对象？

   **响应对象**，包含状态代码和响应文本。

   * `requests.get` 方法返回一个响应对象。此代码将向雅虎发送网络请求！并输出获得的 HTML 和 JavaScript。
   * 不是请求对象，`requests.get` 函数调用的确执行的是请求，但是返回的值不是请求
   * 不是模块对象，`requests` 是模块，但是此代码里的变量 `yahoo` 不是模块。

2. ~~~python
   list =[] #列表元素可以修改
   tuple =() #元组元素不可以修改
   ~~~

3. 添加一个 `try .. except` 语句，以处理发生连接错误的情形

### 11-24 终版天气预报

~~~python
def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()
~~~

如果加入try ... except 判断

~~~python
def fetch_location(query):
    try:
        return requests.get(API_ROOT + API_LOCATION + query).json()
    except requests.Exceptions.ConnectError:
        print('Network have issue.')

    
~~~

但是Dan没加在这里，因为

* 函数最好只做函数名的一件事
* 不止一处会用到网络请求

所以检测加在最终查询函数

~~~python
def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you? ")
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?")

~~~

## 13 对象和类

### 13-1 开始

已经接触过的对象：turtle 字符串 列表 文件 函数，内置于pythoncore 的对象 object

python 允许创建新的自有的对象，使用对象而不用关心内部如何运作

创建新的对象的方式是，编写类定义

### 13-2 复习对象和数据类型

1. while 循环不是对象

   判断是否为对象的方式之一是询问**是否能作为变量的值**。字符串、打开的文件，甚至函数都是对象，但是 while 循环不是。

   * 函数是对象。函数定义会创建函数对象。
   * 打开的文件是对象。当你调用 `open` 函数时，它返回的是打开文件对象。
   * 字符串是对象。你可以将字符串放入变量里，将字符串当做参数传递，返回字符串，等等。

2. 关于对象的表述

   * 每个对象都占据了计算机内存中的某个空间。创建对象时，Python 会为其分配空间。当引用对象的变量超出范围时，Python 可以通过删除不使用的对象释放该内存空间。
   
   * 但是并非所有对象都可修改。例如，字符串和整数不能修改
   
   * 对象可以消失。回忆下函数变量作用域知识。如果对象仅被函数里的变量引用，并且该函数存在，那么该对象可以消失。
   
   * 某些对象不能被修改。
   
     回忆下字符串不变性知识。你可以将字符串对象替换为其他字符串，但是不能更改字符串的值。
   
     整数 `5` 等数字也是不可变的：你可以更改变量引用的数字，但是 `5` 本身不能更改。
   
3. ~~~python
   open("dictionary.txt") 和 myfile.read()
   ~~~

   这两个表达式的结果数据类型不同。`open("dictionary.txt")` 的结果是打开文件对象，如果该文件不存在，则抛出错误。`myfile.read()` 的结果是字符串，假设 `myfile` 是打开文件对象。

4. 关于 数据类型的表述

   * 字符串和列表具有一些相同的方法，例如 `count` 和 `find`。但是字符串类型和列表类型各自包含对方没有的方法。
   * 没有小数部分的数字（例如 `5` 或 `-23`）属于 `int` 数据类型，表示整数。有小数部分的数字（例如 `3.1415` 或 `-0.01`）属于不同的数据类型，叫做 `float`。
   * 文件名是字符串，但是文件对象不是字符串对象类型。文件本身是一种对象，具有的方法和字符串方法截然不同。但是，很多文件对象接受字符串参数或返回字符串值。

### 13-3 对象属于类

每一个对象都有类型，type()函数查看，也就说每个对象都属于一种类class。

比如input 函数一直返回的是字符串的对象

查看函数 isinstance 和 type

#### isinstance 

~~~python
import turtle
george = turtle.Turtle();
isinstance(george,turtle.Turtle)
>>> isinstance(george,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance expected 2 arguments, got 1
~~~

太难用了，自己要给判断。除非要判断的时候

#### type

~~~
>>> type("monkey")
<class 'str'>
~~~

turtle.Tturtle 不是函数，也不是方法。 是类本身，调用就会创建一个。

~~~python
>>> import turtle
>>> amy = turtle.Turtle()

>>> type(amy)
<class 'turtle.Turtle'>
~~~

练习

> `5` 和 `True` 属于 `int` 类。
>
> `True` 属于 `int` 是不是有点让你感到惊讶？`True` 也是布尔值（类 `bool`）。实际上，所有布尔值也是 `int`。稍后在这节课你将知道为何这样。

### 13-4 class在不同的语言

* 在python中 class 类是创建对象的模板或蓝图，通过调用类来使用类，像使用函数和方法一样。调用时，返回这个类的新对象，然后使用这个对象，比如调用这个对象的方法。
* CSS 是一种标签，用于向很多HTML元素 批量引用相同的样式信息
* 类：汽车（发动机+四个轮子）；对象：SUV(外形+大点的轮胎)；方法：越野能力

### 13-5-6 创建新的类

animals.py文件

~~~python
import random

class Dog:
    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "food":
            print("Yummy food!")
        else:
            print("That's not food!")

class Cat:
    def speak(self):
        print(random.choice(["Meow!", "Purr!"]))

~~~

使用方法

~~~python
import animals
black = animals.Dog()
black.eat("wood")
white = animals.Cat()
white.speak()
~~~

* 类里面放的是方法定义 method definition

* def speak(self)  调用时，python会自动传递参数名字比如fido，self是通用名，不是指定的

  如果不给参数

  ~~~python
  >>> import animals
  >>> ty = animals.Cat()
  >>> ty.speak()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: speak() takes 0 positional arguments but 1 was given
  >>> ty.speak(ty)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: speak() takes 0 positional arguments but 2 were given
  ~~~

  

* 引用赋值是记得最后括号 

  ~~~python
  black = animals.Dog()
  ~~~

  不然后面的方法调用会报错

  ~~~python
  >>> white.speak()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: speak() missing 1 required positional argument: 'self'
  ~~~

### 13-7 使用类级别的变量

.py的文件修改不会影响到已经导入的程序，需要退出程序并重启运行才能让改动生效。

~~~python
>>>exit()
python
import animals
~~~

类里面可以有变量，叫做类级别变量

~~~python
class Dog:
    name ='D-O-G,dog.'
~~~

所有调用的参数，都可以用这个方法来调用这个变量。

~~~PYTHON
>>> import animals
>>> black = animals.Dog()
>>> black.name()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> black.name
'D-O-G,dog.'
>>> black.name = 'DOG'
>>> black.name
'DOG'
~~~

### 13-8 使用实例 级别的变量

实例级别变量，主要用于给类的实例针对性的赋值,

~~~python
self.name
~~~

~~~python
import random

class Dog:
    uni_name ='D-O-G'
    def speak(self):
        print("Woof!")
    def learn_name(self,name):
        self.name = name
    def repson(self,words):
        try:
            if self.name in words:
                self.speak()
        except AttributeError:
            print(f"{self} not learn a name.")
    

~~~

练习：

> 银行账户里的资金数量特定于某个银行账户；并没有在 `BankAccount` 类的所有对象之间分享，因此是实例变量。
>
> `UserAccount` 类里的密码最大长度对于该类的所有实例来说都一样，因此是类级别变量。
>
> `ChessGame` 中棋盘上的当前棋子列表特定于一场游戏。每个棋类游戏都有自己的棋盘和棋子。这是实例级别变量。
>
> 所有 `Hexagon` 都具有相同的边数，因此是类级别变量。

~~~python
>>> black.learn_name('Leo')
>>> black.name
'Leo'
>>> black.repson('Good boy,Leo')
Woof!

>>> gary.repson('Good boy,Leo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/workspace/animals.py", line 13, in repson
    if self.name in words:
AttributeError: 'Dog' object has no attribute 'name'
~~~

添加 try except AttributeError:防止中断

### 13-9 初始化 name 

~~~python
__init__ 
~~~

~~~python
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Woof!")
   
        
    def repson(self,words):
        if self.name in words:
            self.speak()
~~~

此时第一次调用时，必须传递name这个参数，并进行初始化

~~~python
black = animals.Dog("Leo")
~~~

不然提示缺少name参数

### 13-10 在实例里存储信息

~~~python
class Dog:
    uni_name ='D-O-G,dog.'
    
    def __init__(self,name):
        self.name =name
        self.i = 0
    
    def count(self):
        self.i +=1
        for n in range(self.i):
            self.speak()
        
        
        
        
    def speak(self):
        print("Woof!")
    def eat(food):
        if food =='food':
            print("Yummy food")
        else:
            print("Not food")
    def learn_name(self,name):
        self.name =name
    def repson(self,words):
        try:
            if self.name in words:
                self.speak()
        except AttributeError:
            print(f"{self} not learn a name.")
    
class Cat:
    def speak(self):
        print("Meow!")
        
# When calling the eat method, you only need to pass it
# one argument, even though there are two parameters:
# spot.eat("biscuit")
# spot.eat("chair")

~~~

* 计数器初始化在init 里初始化为实例变量，而且不是类级别变量

### 13-14 继承 inheritance / subclassing

1. copy已经有的行为
2. 还可以修改和替换已经有的行为

~~~python

class Chihuahua(Dog):
    origin = 'Mexico'
    
    def speak(self):
        print('Yip!')
~~~

~~~python
isinstance(Chihuahua,animals.Dog)
True

issubclass(animals.Chihuahua,animals.Dog)
True
~~~

> 布尔值 True 和 False 也是 int 类的成员。实际上这是一种子类示例，内置在了 Python 的核心代码里。True 和 False 是 `bool` 类的成员 — 但是 `bool` 是 `int` 的子类

练习：

~~~python
class Dog:
    uni_name ='D-O-G,dog.'
    
    def __init__(self,name):
        self.name =name
        self.i = 0
    
    def count(self):
        self.i +=1
        for n in range(self.i):
            self.speak()
        
        
        
        
    def speak(self):
        print("Woof!")
    def eat(food):
        if food =='food':
            print("Yummy food")
        else:
            print("Not food")
    def learn_name(self,name):
        self.name =name
    def repson(self,words):
        try:
            if self.name in words:
                self.speak()
        except AttributeError:
            print(f"{self} not learn a name.")
class Corgi(Dog):
    origin : 'Welsh'
    def speak(self):
        print("Wangwang!")
class Cat:
    def speak(self):
        print("Meow!")
        
# When calling the eat method, you only need to pass it
# one argument, even though there are two parameters:
# spot.eat("biscuit")
# spot.eat("chair")

~~~

~~~python
>>> import animals
>>> Doudou = animals.Corgi("Dou")
>>> Doudou.speak()
Wangwang!
>>> Doudou.name()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> Doudou.uni_name
'D-O-G,dog.'
>>> Doudou.name
'Dou'
>>> Doudou.repson("Hi Doudou")
Wangwang!
~~~

定义的属性，不能括号，不是方法会报错.

#### pass

> 在 Python 里不能有不包含任何语句的函数或类

`pass` 可以用在类或方法定义里，表示意在什么也不做.占位符方法

~~~python
class Dog:
    def do_trick(self):
        pass

class Chihuahua(Dog):
    pass

class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The chihuahua spins in the air and turns briefly into a chicken.")
~~~

~~~python
>>> fido = Dog()
>>> fido.do_trick()
>>> pupper = TrainedChihuahua()
>>> pupper.do_trick()
The chihuahua spins in the air and turns briefly into a chicken.
~~~

### 13-12 关系判断

is-a 和 Has-a

> Husky is a dog
>
> Dog-park is not dog
>
> Dog-park has a dog in it

Has-a 的代码展示

~~~python
class DogPark():
    def __init__(self,dogs):
        self.dogs =dogs
~~~

13-13 super()

在修改父类的init时，需要添加super(). 来继承父类其他的初始化,不是完整的修改了父类的初始化方法，避免报错。

~~~python
import turtle
class myNewTurtle(self,turtle.Turtle):
    def __int__(self):
        super().__init__()
        self.color("orange")
        self.speed(0)
~~~

不是每一个父类都需要，但是我觉得建议这么做，没什么坏处

## 16 爬虫

### 16-2 HTML基础

* `div` 是 "division" 的缩写
* `p` 是 "段落" 的缩写。`` 和其结束标签 `` 之间的文本是提供 HTML 时，显示在屏幕上的内容
* 标签是一个 HTML 源码，而元素是在浏览器呈现标签后用户可以看到的可视化组件。

![img](README.assets/trees.png)

~~~html
<title>My Website</title>
<div id="introduction">
  <p>
    Welcome to my website!
  </p>
</div>    
<div id="image-gallery">
  <p>
    This is my cat!
    <img src="cat.jpg" alt="Meow!">
    <a href="https://en.wikipedia.org/wiki/Cat">Learn more about cats!</a>
  </p>
</div>
~~~

* `image-gallery` div 有一个直接后代元素或子类元素：段落元素。
* 每个元素都有一个父类，这是因为将这些元素建构为一个树。一个元素可以具有任意数量的子类，但只能有一个父类。

* 锚标签（用``表示，用于创建链接）

  ~~~html
  <a href="https://en.wikipedia.org/wiki/Cat">Learn more about cats!</a>
  <!-- href:hypertext reference 超文本引用 -->
  ~~~

#### requests 模块

~~~python
import requests
respone = requests.get('https://udacity.com')
print(respone.text)
>>> print(type(respone))
<class 'requests.models.Response'>
>>> print(type(respone.text))
<class 'str'>
~~~

#### Beautiful Soup

官方使用[指导文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

安装

~~~python
pip3 install beautifulsoup4
or
pip install beautifulsoup4


~~~

>Requirement already satisfied: beautifulsoup4 in c:\users\admin\appdata\local\programs\python\python38\lib\site-packages (4.8.2)
>Requirement already satisfied: soupsieve>=1.2 in c:\users\admin\appdata\local\programs\python\python38\lib\site-packages (from beautifulsoup4) (2.0)

~~~python
import os
import reuqests
from bs4 import BeautifulSoup
magento = requests.get('https://magento.com/tech-resources/download')
webtext = magento.text
magento_soup = BeautifulSoup(webtext,'html.parser')
with open("magento-download-link.txt","w") as newf:
    for link in magento_soup.find_all('a'):
    	hrefs = link.get('href')
        if(type(hrefs)) == str:
			newf.write(f"{hrefs}\n")
    

    

~~~

练习

计算结果为页面中第一段的所有锚标签

~~~python
soup.p.find_all('a')
~~~

如果一个 soup 对象的名称为 `soup`，那么什么代码将选择一个具有 id "image-gallery" 的 div 元素？

~~~python
soup.find(id="image-gallery")
~~~

此代码未明确指定其应该查找一个 div 标签，但是只有一个具有特定 id 的元素，这说明这是正常的。

### 16-3 程序设计

> 1. 打开文章
> 2. 找到文章中的第一个链接
> 3. 单击链接
> 4. 重复此过程，直到找到“哲学”文章或进入文章周期。

程序以此为循环，进行运行，使用while soup.a.name == '哲学'，而不是for循环

1. for循环是确定迭代的一个例子，这意味着如果提前知道循环次数，它们将发挥巨大作用。迭代列表是一个很好的例子，原因是循环列表将针对列表中的每个元素运行一次循环。因为我们不知道找到“哲学”文章需要单击多少次，所以无法确定爬虫的循环次数。
2. 虽然循环对于无限次迭代有用，但是在这种情况中，我们不能预先获取循环次数。因为我们不知道找到“哲学”文章需要单击多少次，所以无法确定爬虫的循环次数。

【说实话，我没看懂上面关于for和while的解释】

> 1. 打开文章
> 2. 找到文章中的第一个链接
> 3. 单击链接
> 4. **在 `article_chain` 数据结构中记录链接**
> 5. 重复此过程，直到我们找到“哲学”文章或进入文章周期。

数据结构中的哪*一*个可以用于 `article_chain`

列表可以以正确的顺序存储文章链，并且可以轻松从列表中选择最后一篇文章。

字典具有无序性，所以难以从链中选择最后一篇文章。

一个元组就可以发挥作用，但并不理想。爬网时，我们将元素添加到链中，但元组具有不可变性。它们没有像某些其他数据结构那样方便的添加方法。

> 1. 查找当前文章 HTML 中的第一个链接
> 2. 下载当前文章的 HTML
> 3. 将当前文章中的第一个链接添加到 `article_chain` 中
>
> 还有一个步骤我们之前尚未明确说明：
>
> 1. 暂停几秒钟，以便不会使请求洪泛维基百科。

伪代码

~~~
页面=一个随机起始页
article_chain = []
而页面标题不是“哲学”，而且我们还没有发现循环：
    将页面添加到 article_chain
    下载页面内容
    在内容中查找第一个链接
    页面=该链接
    暂停片刻
~~~

