fn binary_search(nums: &Vec<i32>, target: i32) -> bool {
    let mut low = 0;
    let mut high = nums.len() as i32 - 1;

    while low <= high {
        let middle = low + (high - low) / 2;
        let middle_val = nums[middle as usize];

        if middle_val == target {
            return true;
        } else if middle_val < target {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }

    false
}

fn main() {
    let arr = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let target = 5;

    let found = binary_search(&arr, target);
    if found {
        println!("The target {} was found in the array.", target);
    } else {
        println!("The target {} was not found in the array.", target);
    }
}
