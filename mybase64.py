import re
import sys

_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '/']

def encode(plain):
	a = ''.join(format(ord(x), '08b') for x in plain)				#ab -> 0110000101100010
	
	if len(plain)%3 == 1: p = "=="							#len(plain) == 3n+1 -> add == 
	elif len(plain)%3 == 2: p = "="							#len(plain) == 3n+2 -> add =
	else: p = ""
	
	b = re.findall("......", a + ''.join('0' for x in range(0,(6-len(a)%6))))	#split 6bit, add 0
	c = ''.join(_list[int(i,2)] for i in b) + p 					#convert to string with _list, add =
	return c

def decode(cipher):
	a = [str(_list.index(i)) for i in cipher if i != "="]				#remove "=", convert with _list					
	b = re.findall("........", ''.join(format(int(x), '06b') for x in a))		#convert to 6bit to 8bit
	c = ''.join(chr(int(i,2)) for i in b)						#convert to string
	return c
