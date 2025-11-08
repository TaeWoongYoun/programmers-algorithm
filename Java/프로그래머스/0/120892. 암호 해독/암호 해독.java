class Solution {
    public String solution(String cipher, int code) {
        StringBuilder answer = new StringBuilder();
        for (int i = code - 1; i < cipher.length(); i += code ) answer.append(cipher.charAt(i));
        return answer.toString();
    }
}