class Solution {
    public String longestCommonPrefix(String[] strs) {
        int count = 1;
        String checkedPrefix = "";
        String finalPrefix = "";
        try {
            for (int i = 0; i < strs[0].length(); i++) {
                checkedPrefix = String.valueOf(strs[0].charAt(i));
                count = 0;
                while (count < strs.length){
                    if (strs[count].charAt(i) == checkedPrefix.charAt(0)){
                        count++;
                        if (count == strs.length){
                            finalPrefix = finalPrefix.concat(checkedPrefix);
                            break;
                        }
                    } else {
                        return finalPrefix;
                    }
                }
            }
        } catch (StringIndexOutOfBoundsException|ArrayIndexOutOfBoundsException e){
            if (finalPrefix.length() >= checkedPrefix.length()){
                return finalPrefix;
            } else {
                return "";
            }
        }
        return finalPrefix;
    }
}