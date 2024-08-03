class Solution:
    def reverseWords(self, s: str) -> str:
        lstr = s.split() #splits the strings into list of words
        revlst = lstr[::-1] #reverse the list
        return " ".join(revlst) #joins the reversed list of words into single string with a single space in between
