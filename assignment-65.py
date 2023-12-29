text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
end = text.find("5")
x = text[pos:end+1]
print(float(x))
