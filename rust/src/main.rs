use std::fs::File;
use std::fs;
use std::io::{self, BufRead};
use std::path::Path;

extern crate reqwest;


fn main() {
    let mut data = String::new();
    if let Ok(lines) = read_lines("../sources.txt") {
        for line in lines {
            if let Ok(url) = line {
                println!("Fetching {}", url);
                data.push_str("\n");
                data.push_str(fetch(url).as_str());
            }
        }
    }
    println!("Finished fetching lets store");

    fs::write("ads_list.txt", data).expect("Unable to write file");
    println!("{}", "Done");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn fetch(url: String) -> String {
    let request = reqwest::get(&url);
    return request.unwrap().text_with_charset("utf-8").unwrap();
}