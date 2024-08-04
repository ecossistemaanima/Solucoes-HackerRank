fn staircase(n: usize) {
    for level in 1..=n {
        let spaces = n - level;
        let hashes = level;
        let space_str = " ".repeat(spaces);
        let hash_str = "#".repeat(hashes);
        println!("{}{}", space_str, hash_str);
    }
}

fn main() {
    let n = 6;
    staircase(n);
}