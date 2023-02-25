use std::collections::HashMap;

use crate::solution::{Solution, SolutionInput};
use anyhow::{Ok, Result};
mod hero;
mod valve;
use hero::Hero;
use valve::Valve;
pub struct Day16Pt1;

impl Solution for Day16Pt1 {
    const DAY: usize = 16;
    const PART: usize = 1;

    type TInput = HashMap<String, Valve>;
    type TOutput = usize;

    fn solve(input: &Self::TInput) -> Result<Self::TOutput> {
        // let mut hero: Hero = Hero::new(input.clone())?;
        // hero.release_preassure_in_time(2)?;
        let time = 3;

        let mut preassures_in_time: HashMap<(String, usize), isize> = HashMap::new();

        for i in 1..time {
            for (name, valve) in input {
                preassures_in_time.insert((name.to_string(), i), -1);
            }
        }

        dbg!(preassures_in_time);
        Ok(1)
    }
}

fn get_preassure_for_valve_in_time(
    valve_name: String,
    valves: &Vec<Valve>,
    time_left: usize,
) -> Result<()> {
    //
    // if time_left == 1 {
    //     if valves.get(index)
    // }
    Ok(())
}

impl SolutionInput for HashMap<String, Valve> {
    fn parse(input_str: &str) -> Result<Self> {
        let mut map: HashMap<String, Valve> = HashMap::new();
        let valves = input_str
            .split("\n")
            .map(|x| x.parse().unwrap())
            .collect::<Vec<Valve>>();

        for v in valves {
            map.insert(v.name.clone(), v.clone());
        }
        Ok(map)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use crate::common::get_input;
    use lazy_static::lazy_static;

    lazy_static! {
        static ref INPUT_TEST: HashMap<String, Valve> = get_input::<Day16Pt1>("test.txt").unwrap();
        static ref INPUT_MAIN: HashMap<String, Valve> = get_input::<Day16Pt1>("input.txt").unwrap();
    }

    #[test]
    fn test_part1_test() -> Result<()> {
        assert_eq!(1651, Day16Pt1::solve(&INPUT_TEST)?);
        Ok(())
    }

    // #[test]
    // fn test_part1_result() -> Result<()> {
    //     assert_eq!(339, Day13Pt1::solve(&INPUT_MAIN)?);
    //     Ok(())
    // }

    // #[test]
    // fn test_part2_test() -> Result<()> {
    //     assert_eq!(29, Day12Pt2::solve(&INPUT_TEST)?);
    //     Ok(())
    // }
    // #[test]
    // fn test_part2_result() -> Result<()> {
    //     assert_eq!(332, Day12Pt2::solve(&INPUT_MAIN)?);
    //     Ok(())
    // }
}
