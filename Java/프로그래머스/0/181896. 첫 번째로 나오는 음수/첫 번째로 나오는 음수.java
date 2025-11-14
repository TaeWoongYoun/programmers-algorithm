class Solution {
    public int solution(int[] num_list) {
        for (int i = 0; i < num_list.length; i++) if (0 > num_list[i]) return i;
        return -1;
    }
}