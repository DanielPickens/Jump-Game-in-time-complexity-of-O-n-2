int minJump(int[] num, int n){
    int[n] minJumps = {INT_MAX}
    minJumps[0] = 0
    for(i = 0 to i < n){
        for(j = i+1 to j < min(i+num[i]+1, n)) {
            minJumps[j] = min(minJumps[j], 1 + minJumps[i])
        }
    }
    return minJumps[n-1]
