text = "X-DSPAM-Confidence:    0.8475"
intPos = text.find(':')
piece = text[intPos+1:]
end = float(piece)
print(end)
