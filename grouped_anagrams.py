from collections import defaultdict 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # anagrams_mapping = {}
        # for word in strs:
        #     sorted_str = "".join(sorted(word))
        #     if sorted_str in anagrams_mapping:
        #         anagrams_mapping[sorted_str].append(word)
        #     else:
        #         anagrams_mapping[sorted_str] = [word]
        
        # return list(anagrams_mapping.values())


        # anagrams_map = {}
        anagrams_map = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1
            count = tuple(count)
            # if count in anagrams_map:
            #     anagrams_map[count].append(word)
            # else:
            #     anagrams_map[count] = [word]
            anagrams_map[count].append(word) 
            
        return list(anagrams_map.values())



def test_solution(input,output):
    solution = Solution()
    
    response = solution.groupAnagrams(input)
    # exit(1)
    # Process the response to sort inner lists and then the outer list
    processed_response = [sorted(group) for group in response]
    processed_response = sorted(processed_response)

    # Similarly, process the expected result
    processed_expected = [sorted(group) for group in output]
    processed_expected = sorted(processed_expected)

    assert processed_response == processed_expected, f"Expected {processed_expected} but got {response}"
    print("Test passed successfully!")


input = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]
test_solution(input,output)


input = [""]
output = [[""]]
test_solution(input,output)

input = ["a"]
output = [["a"]]
test_solution(input,output)

# Sample test
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
