class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for group in zip(*strs):  # groups like ('f','f','f'), ('l','l','l'), ('o','o','i'), ...
            if len(set(group)) == 1:  # all characters same
                prefix += group[0]
            else:
                break
        return prefix

        