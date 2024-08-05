fn gradingStudents(grades: &mut [i32]) -> &mut [i32] {
    for grade in grades.iter_mut() {
        if *grade >= 38 {
            let rest = 5 - (*grade % 5);
            if rest < 3 {
                *grade += rest;
            }
        }
    }
    grades
}

fn main() {
    let mut arr = [73, 67, 38, 33];
    let result = gradingStudents(&mut arr);
    println!("{:?}", result);
}
