fn plus_minus(arr: &[i32]) {
    let n = arr.len() as f64;

    let positive_v = arr.iter().filter(|&&x| x > 0).count() as f64;
    let negative_v = arr.iter().filter(|&&x| x < 0).count() as f64;
    let zeros = arr.iter().filter(|&&x| x == 0).count() as f64;

    println!("{:.6}", positive_v / n);
    println!("{:.6}", negative_v / n);
    println!("{:.6}", zeros / n);
}

fn main() {
    let arr = [1, -2, 0, 3, -4, 0];
    plus_minus(&arr);
}
