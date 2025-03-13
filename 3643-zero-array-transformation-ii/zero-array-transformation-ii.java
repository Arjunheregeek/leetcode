class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        if (!willBeZero(nums, queries, queries.length)) {
            return -1;
        }
        int lo = 0, hi = queries.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (willBeZero(nums, queries, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return hi;
    }
    
    private boolean willBeZero(int[] arr, int[][] queries, int k) {
        int[] d = new int[arr.length + 1];
        for (int i = 0; i < k; i++) {
            int[] q = queries[i];
            int l = q[0], r = q[1], val = q[2];
            d[l] += val;
            d[r + 1] -= val;
        }
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += d[i];
            if (arr[i] > sum) {
                return false;
            }
        }
        return true;
        
    }
}