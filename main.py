def main():
	print('Hello, world!')
	foo()
	arr = [" "] * 9 

	print("Welcome to Tic Tac Toe!")
	arr[0] = "X"
	printBoard(arr)


def foo(): 
	print(1+1)


def printBoard(arr):
    print('    |    |')
    print('  ' + arr[0] + ' | ' + arr[1] + '  | ' + arr[2])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + arr[3] + ' | ' + arr[4] + '  | ' + arr[5])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + arr[6] + ' | ' + arr[7] + '  | ' + arr[8])
    print('    |    |')


if __name__ == '__main__':
	main()
