import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        if (s.length() % 2 != 0){
            return false;
        }else {
            for (int i = 0; i < s.length(); i++){
                if (s.charAt(i) == '{' || s.charAt(i) == '[' || s.charAt(i) == '('){
                    stack.push(s.charAt(i));
                }
                if (s.charAt(i) == '}'){
                    if (stack.empty()){
                        return false;
                    }else {
                        if (stack.peek() == '{'){
                            stack.pop();
                        }else {
                            return false;
                        }
                    }
                }
                if (s.charAt(i) == ']'){
                    if (stack.empty()){
                        return false;
                    }else {
                        if (stack.peek() == '['){
                            stack.pop();
                        }else {
                            return false;
                        }
                    }
                }
                if (s.charAt(i) == ')'){
                    if (stack.empty()){
                        return false;
                    }else {
                        if (stack.peek() == '('){
                            stack.pop();
                        }else {
                            return false;
                        }
                    }
                }
            }
        }
        return stack.empty();
    }
}