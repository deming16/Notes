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

## Underscorify Substring
```
Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores. 

If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost substring. If the main string doesn't contain the other string at all, the function should return the main string intact.

Sample Input
string = "testthis is a testtest to see if testestest it works"
substring = "test"

Sample Output
"_test_this is a _testtest_ to see if _testestest_ it works"
```
```python
def underscorifySubstring(string, substring):
	locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)

def getLocations(string, substring):
	locations = []
	startIdx = 0
	while startIdx < len(string):
		nextIdx = string.find(substring, startIdx)
		if nextIdx != -1:
			locations.append([nextIdx, nextIdx + len(substring)])
			startIdx = nextIdx + 1
		else:
			break
	return locations

def collapse(locations):
	if len(locations) == 0:
		return locations
	newLocations = [locations[0]]
	
	previous = newLocations[0]
	for i in range(1, len(locations)):
		current = locations[i]
		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			newLocations.append(current)
			previous = current
	return newLocations

def underscorify(string, locations):
	res = []
	locationIdx = 0
	stringIdx = 0
	betweenUnderscore = False
	while stringIdx < len(string) and locationIdx < len(locations):
		if betweenUnderscore:
			if stringIdx == locations[locationIdx][1]:
				res.append("_")
				betweenUnderscore = False
				locationIdx += 1
		else:
			if stringIdx == locations[locationIdx][0]:
				res.append("_")
				betweenUnderscore = True
		res.append(string[stringIdx])
		stringIdx += 1
	
	# case 1 underscores are done so just concat rest of string
	if stringIdx < len(string):
		res.append(string[stringIdx:])
	# case 2 string has finished while doing the last location
	# ooncat closing underscore
	if locationIdx < len(locations):
		res.append("_")
	return "".join(res)
```
