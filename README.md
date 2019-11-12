# udacity-python-28-days
learn Python on Udacity

[toc]

> 下线运行python 推荐网站 https://trinket.io/

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

对叫做*amy*的Turtle对象调用*foroerd*方法，并为其输入100



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
>     amy.forward(100)
>     amy.right(72)
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
>           135, 0, 0, 0, 
>           90, 0, 0, 0,
>           135, -90, 0, 0,
>           90, 0, 0, 0]
> for angle in angles:
>     # Turn right, then go forward 25.
>     # (How far to turn?
>     #  Use the angle variable!)
>     builder.right(angle)
>     builder.forward(25)
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

> 多边形移动角度，是360除以形状的编书。

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

(图片真实存在。如果看不到图片，因为总所周知的原因，你可能要想点办法)

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

2. 运行函数定义 draw_squre 【全局】，讲函数主体所有代码放入内存，并与之关联、

3. 定义函数 draw_flower【全局】，(代码只是被保存，没有实际运行)

4. 调用函数 draw_flower，size = 100, petals = 99

5. 然后调用turtle 函数 创建Turtle对象，并保存到doodler 变量中

6. 改变颜色和宽度

7. 进入for循环，range出 0-6的7个数字

8. 调用draw_square全局变量，传入doodler和 100，赋值给形参length 100.

   draw_square 是看不到petals的，因为petals是draw_flower的局部变量

![](.\screenshots\draw_flowers.png)

