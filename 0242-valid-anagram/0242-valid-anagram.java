class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();

        if (s.length() != t.length()){
            return false;
        }

        for(char ch : s.toCharArray()){
            if(!map.containsKey(ch)){
                map.put(ch, 1);
            }else{
                map.put(ch, map.get(ch) + 1);
            }
        }

        for(char ch : t.toCharArray()){
            if(!map.containsKey(ch)){
                return false;
            }
            else{
                map.put(ch, map.get(ch) - 1);
            }
        }

        for(char key : map.keySet()){
            if (map.get(key)  != 0){
                return false;
            }
        }

        return true;
    }
}