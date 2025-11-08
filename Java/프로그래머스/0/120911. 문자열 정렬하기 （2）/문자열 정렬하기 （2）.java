import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String[] strArr = my_string.toLowerCase().split("");
        Arrays.sort(strArr);
        return String.join("", strArr);
    }
}