fn mini_max_sum(arr: Vec<usize>) {
    let total_sum: u64 = arr.iter().map(|&x| x as u64).sum();
    let mut min_sum = u64::MAX;
    let mut max_sum = u64::MIN;

    for &num in arr.iter() {
        let current_sum = total_sum - num as u64;
        min_sum = min_sum.min(current_sum);
        max_sum = max_sum.max(current_sum);
    }

    println!("{} {}", min_sum, max_sum);
}

// Alternative Version:
fn mini_max_sum(arr: Vec<i32>) {
    let length = arr.len() - 1;
    let mut max = arr[0];
    let mut min = arr[0];
    let mut sum = 0;

    for &num in arr.iter() {
        if num > max {
            max = num;
        }
        if num < min {
            min = num;
        }
    }

    for &num in arr.iter() {
        sum += num;
    }

    println!("{} {}", sum - max, sum - min);
}

fn main() {
    let arr = vec![1, 3, 5, 7, 9];
    mini_max_sum(arr);
}