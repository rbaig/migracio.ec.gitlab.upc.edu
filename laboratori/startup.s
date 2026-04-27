###################################
# Standard startup code.  Invokes the routine "main"
# and calls exit() on return from main
.text
.globl __start
__start:
	jal	main

	li	a7, 10		# Service number in register a7; 10 (exit)
	ecall
