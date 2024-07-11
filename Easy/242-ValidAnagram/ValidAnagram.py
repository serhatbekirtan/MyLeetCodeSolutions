class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def build_map(string):
            map = {}
            i = 0

            while i < len(string):
                key = string[i]
                if not key in map:
                    map[key] = 1
                else:
                    map[key] += 1
                
                i += 1
            
            return map

        def check_anagram(map1, map2) -> bool:
            for key in map1:
                if not key in map2 or map1[key] != map2[key]:
                    return False
            
            return True
        
        map_s = build_map(s)
        map_t = build_map(t)
        
        return check_anagram(map_s, map_t)
    

    # Alternate solutions(more like cheating):
      # return Counter(s) == Counter(t)
    
      # return sorted(s) == sorted(t)