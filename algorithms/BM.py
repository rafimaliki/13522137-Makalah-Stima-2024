__package__ = "algorithms"

from typing import List
from algorithms.MyRegex import MyRegex
import time

class BM: 
    
    def find_multiple_matches(text: str, pattern: str) -> int:
        
        start_time = time.time()
        
        list_match = []
        list_match.append(BM.match(text, pattern))
        
        while (list_match[-1] != -1):
            text = text[list_match[-1] + 1:]
            list_match.append(BM.match(text, pattern))
            
        list_match = list_match[:-1]

        return len(list_match)
    
    def match(text: str, pattern: str) -> int:
        
        if not text or not pattern:
            return -1
        
        text = str(text)
        MyRegex.lower(str(pattern))
        
        last = BM.__computeLast(pattern)
        
        n = len(text)
        m = len(pattern)

        i = m - 1
        
        if (i > n - 1):
            return -1

        j = m - 1

        while True:
            if (pattern[j] == text[i]):
                if (j == 0):
                    return i
                else:
                    i -= 1
                    j -= 1
            else:
                lo = last.get(text[i], -1)
                i = i + m - min(j, 1 + lo)
                j = m - 1
                
            if (i > n - 1):
                break
        
        return -1
    
    def __computeLast(pattern: str) -> dict:
        last = {}
        
        m = len(pattern)
        
        for i in range(m):
            last[pattern[i]] = i
        
        return last