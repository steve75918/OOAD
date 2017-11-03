text = "X-DSPAM-Confidence:    0.8475";

pos = text.find('0')
fval = float(text[pos:])

print(fval)