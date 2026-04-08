def genParenthesis(ans, n, curr, open_used, close_used):
    
    # base case
    if len(curr) == 2 * n:
        ans.append(curr)
        return
    
    # add '(' if we still can
    if open_used < n:
        genParenthesis(ans, n, curr + '(', open_used + 1, close_used)
    
    # add ')' only if valid
    if close_used < open_used:
        genParenthesis(ans, n, curr + ')', open_used, close_used + 1)


ans = []
genParenthesis(ans, 3, '', 0, 0)
print(ans)