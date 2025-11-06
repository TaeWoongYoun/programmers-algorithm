class Solution {
    public int solution(int[] array, int height) {
        int length = array.length;
        int answer = 0;
        for (int i = 0; i < length; i++){
            if (array[i] > height) {
                answer += 1;
            }
        }
        return answer;
    }
}