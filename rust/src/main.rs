use std::fs::File;
use std::fs;
use std::io::{self, BufRead};
use std::path::Path;
use std::io::Read;

extern crate reqwest;


fn main() {
    let data = "Mandje";
    if let Ok(lines) = read_lines("../sources.txt") {
        for line in lines {
            if let Ok(url) = line {
                println!("{}", url);
                fetch(url);
            }
        }
    }
    fs::write("ads_list.txt", data).expect("Unable to write file");
    println!("{}", "Done");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn fetch(url: String) -> Result<(), Box<dyn std::error::Error>> {
    println!("url: {}", url);

    let content = reqwest::get(&url)?.text_with_charset("utf-8")?;

    println!("url: {}", content);
    Ok(())
}