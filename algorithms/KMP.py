__package__ = "algorithms"

from typing import List
from algorithms.MyRegex import MyRegex
import time

class KMP:
    
    def find_multiple_matches(text: str, pattern: str) -> int:
        
        start_time = time.time()
        
        list_match = []
        list_match.append(KMP.match(text, pattern))
        
        while (list_match[-1] != -1):
            text = text[list_match[-1] + 1:]
            list_match.append(KMP.match(text, pattern))
            
        list_match = list_match[:-1]
        
        return len(list_match)
    
        
    def match(text: str, pattern: str) -> int:
        
        if not text or not pattern:
            return -1
        
        text = str(text)
        pattern = MyRegex.lower(str(pattern))
        
        b = KMP.__computeBorder(pattern)
        
        n = len(text)
        m = len(pattern)
        
        i = 0
        j = 0
        
        while (i < n):
            if (text[i] == pattern[j]):
                if (j == m - 1):
                    return i - m + 1
                i += 1
                j += 1
            elif (j > 0):
                j = b[j - 1]
            else:
                i += 1
        
        return -1
                
    def __computeBorder(pattern: str) -> List[int]:
        b = [0] * len(pattern)
        
        m = len(pattern)
        j = 0
        i = 1
        
        while (i < m):
            if (pattern[i] == pattern[j]):
                j += 1
                b[i] = j
                i += 1
            elif (j > 0):
                j = b[j - 1]
            else:
                b[i] = 0
                i += 1
                
        return b
        