__package__ = "algorithms"

from excluded_words.excluded_words import excluded_words, symbols
from algorithms.KMP import KMP
from algorithms.BM import BM
import time

import itertools

class WordCounter:

    def countUniqueWords(text: str, method: int):
        if not text:
            return {}
        
        start_time = time.time()
        
        word_count = {}
        
        idx = 0
        while idx < len(text):
            
            pattern = ""
            
            while idx < len(text) and text[idx] != " " and text[idx] != "\n" and text[idx] != "\t" and text[idx] not in symbols:
                pattern += text[idx]
                idx += 1
            
            if pattern not in word_count and pattern not in excluded_words and pattern != "" and len(pattern) > 2:
               
                if method == "1":
                    word_count[pattern] = KMP.find_multiple_matches(text, pattern)
                else:
                    word_count[pattern] = BM.find_multiple_matches(text, pattern)
                    
            idx += 1
                    
                        
        word_count = {word: count for word, count in word_count.items() if word not in excluded_words}

        keys_to_remove = set()
        for word1 in word_count:
            for word2 in word_count:
                
                if word1!= word2 and word1 in word2 and word1 not in keys_to_remove and word2 not in keys_to_remove and word2 != "kesimpulan":
                    
                    word_count[word2] = max(word_count[word1], word_count[word2])
                    keys_to_remove.add(word1)
                    
                    if word1 == "denga":
                        print('denga', word_count[word1], word_count[word2])
                        
                    break
                        
                
        for key in keys_to_remove:
            del word_count[key]
        
        
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        
        
        print("\n10 kata paling sering muncul:")
        for word, count in itertools.islice(sorted_word_count.items(), 10):
            print(f"  {word}: {count} (Signifikansi: {count/len(text.split())*100:.2f}%)")
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        if method == "1":
            print(f"\nWaktu eksekusi menggunakan KMP: {execution_time:.2f} ms")
        else:
            print(f"\nWaktu eksekusi menggunakan BM: {execution_time:.2f} ms")