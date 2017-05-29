import json
import requests


topWR = open("top.txt", "r")
champdata = topWR.readlines()

for line in champdata:
    words = line.split()
print (words)
