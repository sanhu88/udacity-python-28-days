def total_of_all():
    x = 0
    data= []
    prompt  = "请输入数字进行合计计算:"
    prompt2 = "请输入有效的数字或者输入q退出. "
    while True:
      a = input(prompt)
      if a == 'q':  # 输入q退出
          break
      if not a.isdigit():
        print('请输入有效的数字或者输入q退出！！！')
        continue
      data.append(int(a))
    x = sum(data)
    print("合计结果是：",x)
total_of_all()