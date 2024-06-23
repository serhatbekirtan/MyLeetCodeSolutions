class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        if (x == 0){
            return true;
        }
        if (x % 10 == 0){
            return false;
        }
    
        int comparableNumber = x;
        int reversed = 0;
        while (x >= 10){
            reversed += x % 10;
            x = x / 10;
            reversed = reversed * 10;
        }
        reversed = reversed + x;
        return comparableNumber == reversed;
    }
}