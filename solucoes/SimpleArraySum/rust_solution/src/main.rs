fn simpleArraySum(arr: Vec<usize>) -> usize{
    // Usando built-in methods
    //return arr.iter().sum();

    let mut sum: usize = 0;

    for n in arr.iter(){
        sum += n
    }

    sum
}

fn main() {
    let arr = Vec::from([1, 2, 3]);
    let result = simpleArraySum(arr);
    println!("{}", result);
}
