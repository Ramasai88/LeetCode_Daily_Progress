class Solution {
    public int reverse(int x) {
        long a=Math.abs(x);
        long r=0;
        while(a>0){
            long k=a%10;
            r=r*10+k;
            a/=10;
        }
        if(r>Integer.MAX_VALUE || r<Integer.MIN_VALUE){
            return 0;
        }
        if(x>0){
            return (int)r;
        }
        else{
            return (int)(-1*r);
        }
        
    }
}