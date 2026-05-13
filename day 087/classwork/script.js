function even_or_odd(n){

    if (n % 2 == 0){
        return "Even"
    } else {
        return "Odd"
    }
}

const func = even_or_odd;
console.log(func([5]))


function func1(list1){
    res = []
    for (let i = 0; i < list1.length; i++)
        if (list1[i] % 2 == 0){
            res.push("Even")
        } else{
            res.push("Odd")
        }
    return res
}

function listmap(arr,func1){
    return func1(arr)
}

const x = listmap([2,5,6,7,8],func1)
console.log(x)