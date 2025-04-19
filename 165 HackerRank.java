// 100% HackerRank

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        int totalT = 4 * n;
        int[] t = new int[totalT];
        
        long s = 290797;
        for (int i = 0; i < totalT; i++) {
            s = (s * s) % 50515093;
            t[i] = (int)(s % 500);
        }

        int[][] x = new int[n][2], y = new int[n][2];
        for (int i = 0; i < n; i++) {
            x[i][0] = t[4*i];
            y[i][0] = t[4*i + 1];
            x[i][1] = t[4*i + 2];
            y[i][1] = t[4*i + 3];
        }

        HashSet<Point> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long x1 = x[i][0], y1 = y[i][0];
                long x2 = x[i][1], y2 = y[i][1];
                long x3 = x[j][0], y3 = y[j][0];
                long x4 = x[j][1], y4 = y[j][1];

                long dx1 = x2 - x1, dy1 = y2 - y1;
                long dx2 = x4 - x3, dy2 = y4 - y3;
                long D = dx1 * dy2 - dy1 * dx2;
                if (D == 0) continue;  // parallel or collinear

                long rNum = (x3 - x1) * dy2 - (y3 - y1) * dx2;
                long sNum = (x3 - x1) * dy1 - (y3 - y1) * dx1;

                if (! ( (rNum > 0 && rNum < D) || (rNum < 0 && rNum > D) )) continue;
                if (! ( (sNum > 0 && sNum < D) || (sNum < 0 && sNum > D) )) continue;

                long den = D;
                long xn = x1 * den + rNum * dx1;
                long yn = y1 * den + rNum * dy1;
                if (den < 0) {
                    den = -den;
                    xn = -xn;
                    yn = -yn;
                }

                long g1 = gcd(Math.abs(xn), den);
                long xNum = xn / g1;
                long xDen = den / g1;
                long g2 = gcd(Math.abs(yn), den);
                long yNum = yn / g2;
                long yDen = den / g2;

                set.add(new Point(xNum, xDen, yNum, yDen));
            }
        }

        System.out.println(set.size());
    }

    static class Point {
        long xn, xd, yn, yd;
        Point(long xn, long xd, long yn, long yd) {
            this.xn = xn;  this.xd = xd;
            this.yn = yn;  this.yd = yd;
        }
        @Override public boolean equals(Object o) {
            if (!(o instanceof Point)) return false;
            Point p = (Point)o;
            return xn==p.xn && xd==p.xd && yn==p.yn && yd==p.yd;
        }
        @Override public int hashCode() {
            return Objects.hash(xn, xd, yn, yd);
        }
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
