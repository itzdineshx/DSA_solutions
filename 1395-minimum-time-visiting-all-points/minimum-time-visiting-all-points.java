class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int min_cost = 0; // Initial time
        for (int i = 0; i < points.length - 1; i++){
            int curr_x = points[i][0];
            int curr_y = points[i][1];
            int targ_x = points[i+1][0];
            int targ_y = points[i+1][1];

            min_cost += Math.max(Math.abs(targ_x - curr_x), Math.abs(targ_y - curr_y));
        }
        return min_cost;
    }
}