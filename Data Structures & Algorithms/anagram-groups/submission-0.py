class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = defaultdict(list)
        for string in strs:
            letter_list = [0] * 26
            for char in string:
                letter_list[ord(char) - ord('a')] += 1
            answer_dict[tuple(letter_list)].append(string)
        return list(answer_dict.values())