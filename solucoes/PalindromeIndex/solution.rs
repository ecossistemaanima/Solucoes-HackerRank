fn is_palindrome(s: &str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    for i in 0..n / 2 {
        if chars[i] != chars[n - i - 1] {
            return false;
        }
    }
    true
}

fn palindrome_index(s: &str) -> i32 {
    let chars: Vec<char> = s.chars().collect();
    let mut l = 0;
    let mut r = chars.len() - 1;

    while l < r {
        if chars[l] != chars[r] {
            if is_palindrome(&s[l + 1..=r]) {
                return l as i32;
            }
            if is_palindrome(&s[l..r]) {
                return r as i32;
            }
            return -1;
        }
        l += 1;
        r -= 1;
    }
    -1
}

fn main() {
    println!("{}", palindrome_index("aaab"));
}