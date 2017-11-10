import java.util.*;

public class Problem_G {
    public static class Gem{
        int x;
        int y;

        public Gem(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class compareY implements Comparator<Gem>{
        @Override
        public int compare(Gem e1, Gem e2) {
            return e1.y - e2.y;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int r = scanner.nextInt();
        int w = scanner.nextInt();
        int h = scanner.nextInt();
        List<Gem> gems = new ArrayList<Gem>();
        List<Integer> maxValues = new ArrayList<Integer>();
        for (int t = 0; t < n; t++) {
            gems.add(new Gem(scanner.nextInt(), scanner.nextInt()));
            maxValues.add(0);
        }
        gems.sort(new compareY());
        for (int i = 0; i < n; i++) {
            int max = 1;
            for (int j = 0; j < i; j++) {
                if ((gems.get(i).x - gems.get(j).x) <= (gems.get(i).y - gems.get(j).y) * r) {
                    if (maxValues.get(j) + 1 > max) {
                        max = maxValues.get(j) + 1;
                    }
                }
            }
           maxValues.set(i, max);
        }
        int max = maxValues.get(1);
        for (int i = 0; i < n; i++) {
            if (maxValues.get(i) > max) {
                max = maxValues.get(i);
            }
        }
        System.out.print(max);
    }
}
