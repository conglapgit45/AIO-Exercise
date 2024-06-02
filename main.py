import math
import random


# 1. Viết function thực hiện đánh giá classification model bằng F1-Score.
def calc_f1_score(tp, fp, fn):
    if type(tp) != int or type(fp) != int or type(fp) != int:
        print('tp and fp and fn must be int')
        return
    if tp <= 0 or fp <= 0 or fp <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f'Precision is {precision}')
    print(f'Recall is {recall}')
    print(f'F1_Score is {f1_score}')


# 2. Viết function mô phỏng theo 3 activation function.
def is_number(n):
    try :
        float(n) # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def calc_activation_func(x, activation_function_name):
    if is_number(x) == False:
        print('x must be a number')
        return
    x = float(x)
    
    if activation_function_name == 'sigmoid':
        y = 1 / (1 + math.e**(-x))
    elif activation_function_name == 'relu':
        if x <= 0:
            y = 0
        elif x > 0:
            y = x
    elif activation_function_name == 'elu':
        if x <= 0:
            alpha = 0.01
            y = alpha * (math.e**(x) - 1)
        elif x > 0:
            y = x
    else:
        print(f'{activation_function_name} is not supported')
        return
    print(y)


# 3. Viết function lựa chọn regression loss function để tính loss.
def regression_loss(n_sample, loss_name):
	if n_sample.isnumeric() == False:
		print('number of samples must be an integer number')
		return
	else:
		n_sample = int(n_sample)
	loss = 0
	for i in range(n_sample):
		predict = random.uniform(0,10)
		target = random.uniform(0,10)
		if loss_name.upper() == 'MAE':
			loss += abs(target - predict)
		if loss_name.upper() == 'MSE':
			loss += (target - predict)**2
		if loss_name.upper() == 'RMSE':
			loss += math.sqrt((target - predict)**2)
		print(f'loss name: {loss_name}')
		print(f'sample: {i}')
		print(f'pred: {predict}')
		print(f'target: {target}')
		print(f'loss: {loss}')
	if loss_name.upper() == 'RMSE':
		final_loss = loss * math.sqrt(1 / n_sample)
	else:
		final_loss = loss * (1 / n_sample)
	print(f'final_loss: {final_loss}')


# 4. Viết 4 functions để ước lượng các hàm số sau.
def factorial(n):
	result = 1
	for i in range(n):
		result *= (i + 1)
	return result
	
	
def approx_sin(x, n):
	result = 0
	for i in range(n + 1):
		result += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
	print(f'sin: {result}')
	
	
def approx_cos(x, n):
	result = 0
	for i in range(n + 1):
		result += ((-1)**i)*(x**(2*i))/factorial(2*i)
	print(f'cos: {result}')
	
	
def approx_sinh(x, n):
	result = 0
	for i in range(n + 1):
		result += (x**(2*i+1))/factorial(2*i+1)
	print(f'sinh: {result}')
	
	
def approx_cosh(x, n):
	result = 0
	for i in range(n + 1):
		result += (x**(2*i))/factorial(2*i)
	print(f'cosh: {result}')
	

# 5. Viết function thực hiện Mean Difference of nth Root Error.
def MD_nRE(y, y_hat, n, p):
	loss = (y**(1 / n) - y_hat**(1 / n))**p
	print(loss)

	
if __name__ == "__main__":
    # 1. Viết function thực hiện đánh giá classification model bằng F1-Score.
    calc_f1_score(tp = 2, fp = 0 ,fn = 4)

    # 2. Viết function mô phỏng theo 3 activation function.
    calc_activation_func(1.5, 'belu')

    # 3. Viết function lựa chọn regression loss function để tính loss.
    n_sample = input('Input number of samples (integer number) which are generated: ')
    loss_name = input('Input loss name: ')
    regression_loss(n_sample, loss_name)

    # 4. Viết 4 functions để ước lượng các hàm số sau.
    approx_sin(3.14, 10)
    approx_cos(3.14, 10)
    approx_sinh(3.14, 10)
    approx_cosh(3.14, 10)
	
    # 5. Viết function thực hiện Mean Difference of nth Root Error.
    MD_nRE(100, 99.5, 2, 1)