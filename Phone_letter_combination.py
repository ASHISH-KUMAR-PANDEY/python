def letter_combinations(digits):
    res, n, phone = [], len(digits), {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': [
        'j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    def findcombs(i, curr, letter):
        curr += letter
        if i < n:
            for let in phone[digits[i]]:
                findcombs(i + 1, curr, let)
        else:
            res.append(curr)
    findcombs(0, "", "")
    return res if n > 0 else []
