use std::str::FromStr;

use anyhow::{Error, Ok, Result};

#[derive(Debug, Clone)]
pub struct Valve {
    pub name: String,
    open: bool,
    rate: i32,
    pub tunnels_to: Vec<String>,
    open_time: i32,
    pub already_released: i32,
}

impl Valve {
    pub fn new(name: &str, rate: i32, tunnels_to: Vec<String>) -> Self {
        Self {
            name: name.to_string(),
            open: false,
            rate: rate,
            tunnels_to: tunnels_to,
            open_time: 30,
            already_released: 0,
        }
    }

    pub fn open(&mut self, time: i32) -> Result<()> {
        self.open = true;
        self.open_time = time;
        Ok(())
    }

    pub fn get_released_preassure(&self) -> Result<i32> {
        if !self.open {
            panic!("Valve is not open")
        } else {
            Ok(self.rate * (30 - self.open_time))
        }
    }

    // pub fn get_possible_moves(&self, path: Option<Vec<String>>) -> Result<Vec<Vec<String>>> {
    // if path.is_some() {
    //     for t in self.tunnels_to {}
    // }
    // let mut moves = self.tunnels_to.clone();
    // if !self.open {
    //     moves.push(self.name.clone());
    // }
    // Ok(vec![moves])
    // }
}

impl FromStr for Valve {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let x = s.split(";").collect::<Vec<&str>>();
        let name = x[0].split(" ").collect::<Vec<&str>>()[1];
        let rate: i32 = x[0].split("rate=").collect::<Vec<&str>>()[1].parse()?;
        let tunnels_to = x[1].split("valve").collect::<Vec<&str>>()[1]
            .split(" ")
            .map(|x| x.replace(",", ""))
            .filter(|x| x.chars().collect::<Vec<char>>().len() == 2)
            .collect::<Vec<String>>();
        Ok(Self::new(name, rate, tunnels_to))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_released_preassure() -> Result<()> {
        let mut v = Valve::new("AA", 10, vec![]);
        v.open(2)?;

        assert_eq!(10 * (30 - 2), v.get_released_preassure()?);
        Ok(())
    }
}
