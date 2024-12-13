

class Solution {
public:
    long long findScore(vector<int>& nums) {
        int n = nums.size();
        long long score = 0;

        // Min-heap to store (value, index) pairs
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
        vector<bool> visited(n, false); // Tracks visited indices

        // Push all elements into the heap
        for (int i = 0; i < n; ++i) {
            minHeap.push({nums[i], i});
        }

        // Process elements in increasing order of value
        while (!minHeap.empty()) {
            auto [val, index] = minHeap.top();
            minHeap.pop();

            // Skip already visited indices
            if (visited[index]) {
                continue;
            }

            // Add the value to the score
            score += val;

            // Mark current and adjacent indices as visited
            visited[index] = true;
            if (index > 0) {
                visited[index - 1] = true;
            }
            if (index < n - 1) {
                visited[index + 1] = true;
            }
        }

        return score;
    }
};

