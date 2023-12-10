
#This is the part that can be copied at beginning of a program
def repeat(m,n):
	i = 0
	k = 0
	while i < m:
		LOOP.loop()
		if k < n:
			LOOP.subloop()
			k += 1
		elif k == n:
			k = 0
			i += 1
	else:
		print("Loop is complete.")

#This is the program

class LOOP:
	def loop():
		print("Hello")

	def subloop():
		print("!")

repeat(2,3)
