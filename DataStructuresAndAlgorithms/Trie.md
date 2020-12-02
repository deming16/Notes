## Suffix Trie Construction
```
Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the root node of the trie and should support:
  - Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon class instantiation, which should populate the root of the class.
  - Searching for strings in the trie.
Note that every string added to the trie should end with the special endSymbol character: "*".

Sample Input
string = "babc"

Sample Output
{
  "a": {"b": {"c": {"*": true}}},
  "b": {
    "a": {
      "b": {
        "c": {"*": true}
      }
    },
    "c": {"*": true}
  },
  "c": {"*": true}
}
```
```python
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.populateSubstring(i, string)
        pass
	def populateSubstring(self, firstIndex, string):
		node = self.root
		for i in range(firstIndex, len(string)):
			# char not in trie yet, insert
			char = string[i]
			if char not in node:
				node[char] = {}
			node = node[char]
		node[self.endSymbol] = True

    def contains(self, string):
		node = self.root
		for char in string:
			if char not in node:
				return False
			node = node[char]
		
		if self.endSymbol in node:
			return True
		else:
			return False
        pass
```