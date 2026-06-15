//import java.util.HashMap;
class Solution {
    // public int count(String s){
    //     int count = 0;
    //     for(int i=0; i<s.length(); i++){
    //         if(Character.isLetter(s.charAt(i))){
    //             count ++;
    //         }
    //     }
    //     return count;
    // }
    public HashMap<Character, Integer> StringMap(String s){
        HashMap<Character, Integer> Smap = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            char key = s.charAt(i);
            Smap.put(key, Smap.getOrDefault(key,0)+1);
            //int count;
            // if(Character.isLetter(key) && !Smap.containsKey(key)){
            //     ++count;
            //     Smap.put(key,count);
            // } else if(Character.isLetter(key) && Smap.containsKey(key)){
            //     ++count;
            //     Smap.put(key,count);
            // }
        }
        return Smap;
    }
    
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> Smap = StringMap(s);
        HashMap<Character, Integer> Tmap = StringMap(t);

        return Smap.equals(Tmap);
    //     for(HashMap<Character, Integer> map:Smap){
    //         if(Tmap.containsKey(Smap.getKey()) && Tmap.containsValue(Smap.getValue())){
    //             return true;
    //         }
    //     }
    // return false;    
}
}
