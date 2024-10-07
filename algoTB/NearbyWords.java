package spelling;

import java.util.Queue;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class NearbyWords implements SpellingSuggest {
    private static final int THRESHOLD = 1000;

    Dictionary dict;

    public NearbyWords(Dictionary dict) {
        this.dict = dict;
    }

    public List<String> distanceOne(String s, boolean wordsOnly) {
        List<String> retList = new ArrayList<String>();
        insertions(s, retList, wordsOnly);
        substitutions(s, retList, wordsOnly);
        deletions(s, retList, wordsOnly);
        return retList;
    }

    public void substitutions(String s, List<String> currentList, boolean wordsOnly) {
        for (int index = 0; index < s.length(); index++) {
            for (int charCode = (int) 'a'; charCode <= (int) 'z'; charCode++) {
                StringBuffer sb = new StringBuffer(s);
                sb.setCharAt(index, (char) charCode);

                if (!currentList.contains(sb.toString()) &&
                    (!wordsOnly || dict.isWord(sb.toString())) &&
                    !s.equals(sb.toString())) {
                    currentList.add(sb.toString());
                }
            }
        }
    }

    public void insertions(String s, List<String> currentList, boolean wordsOnly) {
        for (int index = 0; index < s.length() + 1; index++) {
            for (int charCode = (int) 'a'; charCode <= (int) 'z'; charCode++) {
                String[] strs = s.split("");
                LinkedList<String> sList = new LinkedList<>(Arrays.asList(strs));
                sList.add(index, Character.toString((char) charCode));

                String newWord = listToString(sList);

                if (!currentList.contains(newWord) &&
                    (!wordsOnly || dict.isWord(newWord)) &&
                    !s.equals(newWord)) {
                    currentList.add(newWord);
                }
            }
        }
    }

    private String listToString(List<String> list) {
        StringBuilder ret = new StringBuilder();
        for (String c : list) {
            ret.append(c);
        }
        return ret.toString();
    }

    public void deletions(String s, List<String> currentList, boolean wordsOnly) {
        for (int index = 0; index < s.length(); index++) {
            String[] strs = s.split("");
            LinkedList<String> sList = new LinkedList<>(Arrays.asList(strs));
            sList.remove(index);
            String newWord = listToString(sList);

            if (!currentList.contains(newWord) &&
                (!wordsOnly || dict.isWord(newWord)) &&
                !s.equals(newWord)) {
                currentList.add(newWord);
            }
        }
    }

    @Override
    public List<String> suggestions(String word, int numSuggestions) {
        Queue<String> queue = new LinkedList<>();     
        Set<String> visited = new HashSet<>();        
        List<String> retList = new LinkedList<>();    

        queue.add(word);
        visited.add(word);

        while (!queue.isEmpty() && retList.size() < numSuggestions) {
            String curr = queue.poll();
            List<String> neighbors = distanceOne(curr, true);

            for (String n : neighbors) {
                if (!visited.contains(n)) {
                    visited.add(n);
                    queue.add(n);
                    if (dict.isWord(n)) {
                        retList.add(n);
                        if (retList.size() >= numSuggestions) {
                            break;
                        }
                    }
                }
            }
        }

        return retList;
    }

    public static void main(String[] args) {
        String word = "i";
        Dictionary d = new DictionaryHashSet();
        DictionaryLoader.loadDictionary(d, "data/dict.txt");
        NearbyWords w = new NearbyWords(d);
        List<String> l = w.distanceOne(word, true);
        System.out.println("One away word Strings for \"" + word + "\" are:");
        System.out.println(l + "\n");

        word = "tailo";
        List<String> suggest = w.suggestions(word, 10);
        System.out.println("Spelling Suggestions for \"" + word + "\" are:");
        System.out.println(suggest);
    }
}