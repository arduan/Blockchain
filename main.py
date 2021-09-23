from blockchain import Blockchain


def main():
	chain = Blockchain()

	n = int(input('Введите количество создаваемых блоков:'))

	for x in range(n):
		data = str(input('Enter data for block {}: '.format(x+1)))
		chain.add_block(data)

	chain.print_blockchain()


if __name__ == '__main__':
	main()