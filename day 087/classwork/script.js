function datvi(n){
    if (n % 2 == 0){
        return "Even"
    } else {
        return "Odd"
    }
}

const func = datvi;
console.log(func(5))