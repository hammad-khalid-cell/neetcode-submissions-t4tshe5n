class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}  # our dictionary of boxes

        for word in strs:
        # Step 1: sort the letters to make a key
            key = "".join(sorted(word))

        # Step 2: put the word into the right box
            if key not in groups:
                groups[key] = []   # create a new box
            groups[key].append(word)

    # Step 3: return just the grouped words
        return list(groups.values())

            