def num_args(func):
	args = []
	found = False
	while not found:
		try:
			func(*args)
			found = True
		except TypeError:
			args.append(2.0)
	return len(args)
