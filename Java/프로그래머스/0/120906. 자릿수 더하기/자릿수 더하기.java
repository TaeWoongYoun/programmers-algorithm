class Solution {
    public int solution(int n) {
        int answer = 0;
        String str_n = String.valueOf(n);
        String[] strArr = str_n.split("");
        int[] intArr = new int[strArr.length];
        for (int i = 0; i < strArr.length; i++) {
            intArr[i] = Integer.parseInt(strArr[i]);
            answer += intArr[i];
        }
        return answer;
    }
}