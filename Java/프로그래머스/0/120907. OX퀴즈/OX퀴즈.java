class Solution {
    public String[] solution(String[] quiz) {
        boolean answer = false;
        for (int i = 0; i < quiz.length; i++) {
            String[] list = quiz[i].split(" ");
            int left = Integer.parseInt(list[0]);
            int right = Integer.parseInt(list[2]);
            int result = Integer.parseInt(list[4]);
            if (list[1].equals("+")) {
                answer = (left + right == result);
                if (answer == true) quiz[i] = "O";
                else quiz[i] = "X";
            } else {
                answer = (left - right == result);
                if (answer == true) quiz[i] = "O";
                else quiz[i] = "X";
            }
        }
        return quiz;
    }
}