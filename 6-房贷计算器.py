def calc_epp(P, R, N, n):
	"""
	计算等额本金下，第 n+1 月的还款额。此时，已有 n 个月完成还款。
	EPP：Equal Principal Payment 等额本金

	计算公式：每月还款金额 = (贷款本金 / 还款月数) + (本金 — 已归还本金累计额) × 每月利率

	输入：
	P：贷款本金总额
	R：月利率
	N：还款月数
	n：第 n 个月

	输出：
	返回 monthly_payment：第 n+1 月的还款额，保留 2 位小数
	"""

	monthly_payment = round((P/N)+(P-((P/N)*n))*R,2) ## TODO：基于等额本金公式计算，注意保留 2 位小数

	return monthly_payment

def calc_elp(P, R, N):
	"""
	计算等额本息下，第 n+1 月的还款额。此时，已有 n 个月完成还款。
	ELP：Equal Loan Payment 等额本息

	计算公式：每月还款额 = [贷款本金 × 月利率 × (1+月利率) ^ 还款月数] ÷ [(1+月利率) ^ 还款月数－1]

	输入：
	P：贷款本金总额
	R：月利率
	N：还款月数

	输出：
	返回 monthly_payment：第 n+1 月的还款额，保留 2 位小数
	"""
	monthly_payment = round((P*R*(1+R)**N)/((1+R)**N-1),2) ## TODO：基于等额本息公式计算，注意保留 2 位小数

	return monthly_payment

def calc_monthly_payment(P, R, N, EPP):
	"""
	按月打印每月的还款额

	输入：
	P：贷款本金总额
	R：月利率
	N：还款月数
	EPP：Equal Principal Payment 等额本金

	输出：
	按月打印每月的还款额

	"""

	monthly_payment_list = []

	if EPP:
		## 使用等额本金公式
		for n in range(N):
			monthly_payment = calc_epp(P, R, N, n) ## TODO：调用函数 calc_epp 计算
			i =n
			print("EPP等额本金:第  %i  月，需要还款 %.2f"%(n, monthly_payment) ) ## TODO：补充信息中的月份和金额
	else:
		#print("等额本息每月，需要还款 %.2f" %( monthly_payment)) 
		## 使用等额本息公式
		#for n in range(N):
		monthly_payment = calc_elp(P, R, N) ## TODO：调用函数 calc_elp 计算
		print("第 %i 月，需要还款 %.2f" %(n, monthly_payment)) ## TODO：补充信息中的月份和金额

## 测试 ##
## 假设贷款本金为 10000, 年利率为 12%，贷款时长为 2 年，按等额本金计算（True）
## 你也可以修改参数进行测试
'''
epp_monthly_pay = calc_epp(10000, 0.01, 24,1)
print("EPP等额本金:",epp_monthly_pay)
print('<br />')
clp_monthly_pay = calc_elp(10000, 0.01, 24)
print("CLP等额本息",clp_monthly_pay)
print('<br />')
'''
calc_monthly_payment(500000, 0.01, 120, 2>1)
