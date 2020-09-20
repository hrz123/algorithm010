class BlackBox {

    int n, m, t, l;
    boolean[] core;
    int[] positive, negative;

    public BlackBox(int n, int m) {
        this.n = n;
        this.m = m;
        l = 2 * n + 2 * m;
        core = new boolean[l];
        t = 0;

        positive = new int[l];
        negative = new int[l];
        for (int i = 0; i < l; i++) {
            positive[i] = (l - i) % l;
            negative[i] = (m * 2 - i + l) % l;
        }
    }

    public int open(int index, int direction) {
        if (!core[index]) {
            t++;
            core[index] = true;
        }
        if (t == 1) return index;
        else {
            do {
                if (direction == 1) index = positive[index];
                else index = negative[index];
                direction = -direction;
            } while (!core[index]);
        }
        return index;
    }

    public void close(int index) {
        core[index] = false;
        t--;
    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = new BlackBox(n, m);
 * int param_1 = obj.open(index,direction);
 * obj.close(index);
 */
