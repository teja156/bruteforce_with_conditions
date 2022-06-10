# First install exrex
# pip install exrex

# Change PASSWD_PATTERN and PASSWORD_TO_BE_FOUND
# PASSWORD PATTERN GOES LIKE THIS: 
# C = Upper case letter
# L = Lower case letter
# S = Special characters
# D = Digits 

import exrex
import time
import datetime

SPECIAL = '!@#$%^&*()_\-=+`~/\\;:.?,<>' + "'" + '"'

def genRegex(PASSWD_PATTERN):
	regex = '^'
	for i in PASSWD_PATTERN:
		if i == 'C':
			# Caps letter
			regex+="[A-Z]"
		elif i == 'L':
			# Small letter
			regex+="[a-z]"
		elif i == 'D':
			# Digit
			regex+="[0-9]"
		elif i == 'S':
			# Special chars
			regex+=f"[{SPECIAL}]"

	regex+="$"
	return regex

if __name__ == "__main__":
	start = int(time.time())
	PASSWD_PATTERN = 'CCDDDDSL'
	PASSWORD_TO_BE_FOUND = 'AR1531&r'
	# First generate a regex based on the password pattern
	regex = genRegex(PASSWD_PATTERN)
	print(f"Regex: {regex}")
	possibilities = exrex.count(regex)
	print(f"Possibilities: {possibilities}\n")

	# Generate all possibilities
	li = exrex.generate(regex)

	count = 0
	for i in li:
		curr_time = int(time.time())
		time_elapsed = str(datetime.timedelta(seconds=(curr_time-start)))
		count+=1
		print(f"Checking: {i}, Checked: {count}, Time elapsed: {time_elapsed}",end='\r\r')
		if i==PASSWORD_TO_BE_FOUND:
			print(f"\n\nFOUND PASSWORD: {i}")
			print(f"TOTAL TIME ELAPSED: {time_elapsed}")
			break











