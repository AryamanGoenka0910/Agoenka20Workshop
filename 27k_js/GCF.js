function gcf(a, b){
    gcf = 0;
    for (let i = 1; i < a + 1; i++){
        if (a % i == 0){
            if (b % i == 0){
                gcf = i;
        }
      }
    }
    return gcf;
}

console.log(gcf(25, 25));
