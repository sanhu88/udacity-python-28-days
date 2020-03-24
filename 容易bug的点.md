1. if 判断时，一个等号，应该使用时**双等号或者三等号**

2. 循环或者判断 缺少最后面的**冒号 :**

3. 缩进

4. 中英文的括号

5. print(target,"show ",total," times in",string) 最原始的打印

   打印变量print(f"{targe} show {count} times in {str}")

   return(f"{targe} show {count} times in {str}") 调用时要打印

   等同于 return("{} show {} times in {}".format(targe,count,str))

   此外还有之前的% ：return("%s show %s times in %s" % (targe,count,str))

   个人还觉得f""好用直观

   ~~~python
   >>> d =2
   >>> print(f"{d} %s"% ('ok'))
   ~~~

6. 使用return返回true或者是false比较对后续使用友好；print对输出友好

7. ~~~
   TypeError: 'type' object is not subscriptable
   出现了这种错误，直接找报错行中的中括号附近有无错误即可。
   ~~~

8. 

