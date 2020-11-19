## Run-Length Encoding
```
Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run. "For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

To make things more complicated, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
```
```python
def runLengthEncoding(string):
    # Write your code here.
	encodedString = []
	length = 1
	
	for index in range(1, len(string)):
		currChar = string[index]
		prevChar = string[index - 1]
		if currChar != prevChar or length == 9:
			encodedString.append(str(length) + prevChar)
			length = 1
		else:
			length += 1
	encodedString.append(str(length) + string[len(string) - 1])
	return "".join(encodedString)
```