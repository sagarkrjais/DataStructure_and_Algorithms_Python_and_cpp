# Python Program to find min Insertion in a string to make it Palindrome.
""" -----------------------------------
Example:
ab : No. of insertion is required 1 (bab)
abcd : No. of insertion is required 3 (dcbabcd)

The Naive recursive program.
--------------------------------------- """

def find_min_insertion(str, l, h):
    # Base Case.
    if l > h:
        return -1
    if l == h:
        return 0
    if l == h - 1:
        return 0 if str[l] == str[h] else 1
    # Check if the first and last char are same 
    # on the basis of the comparison result, deside
    # which subproblem(s) to call.
    if str[l] == str[h]:
        return find_min_insertion(str,l+1,h-1)
    else:
        return min(find_min_insertion(str,l,h-1), find_min_insertion(str,l+1,h)) + 1

# Main Function.
def main():
    s = "abcd"
    n = len(s) - 1
    print(find_min_insertion(s, 0, n))

# Driver Code.
if __name__ == "__main__":
    main()