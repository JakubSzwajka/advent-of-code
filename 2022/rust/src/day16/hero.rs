use std::{collections::HashMap, path};

use super::valve::Valve;
use anyhow::{Ok, Result};

pub struct Hero<'a> {
    spt: Vec<&'a Valve>,
    current_valve: Option<&'a Valve>,
    valves: HashMap<String, Valve>,
}

impl<'a> Hero<'a> {
    pub fn new(valves: HashMap<String, Valve>) -> Result<Self> {
        Ok(Self {
            spt: vec![],
            valves,
            current_valve: None,
        })
    }

    fn do_move(&'a mut self, possible_moves: Vec<String>) -> Result<()> {
        //

        Ok(())
    }

    pub fn release_preassure_in_time(&'a mut self, max_time: i32) -> Result<()> {
        // let mut t = 1;

        // // let start_valve = self.valves.get("AA").unwrap();
        // self.current_valve = Some(self.valves.get("AA").unwrap());
        // self.spt.push(self.current_valve.unwrap());

        // while t <= max_time {
        //     let curr_valve = self.spt.remove(0);
        //     let possible_moves = curr_valve.get_possible_moves()?;

        //     println!(
        //         "minute: {}. Current valve: {} | possible moves: {:?}",
        //         t, curr_valve.name, possible_moves
        //     );
        //     for m in possible_moves {
        //         // self.spt.push(self.valves.get(&m).unwrap())
        //     }
        //     self.spt
        //         .sort_by(|a, b| a.already_released.cmp(&b.already_released));

        //     t += 1;
        // }

        Ok(())
    }

    pub fn get_possible_paths(&'a self, visited2: Vec<String>) -> Result<Vec<Vec<String>>> {
        // visited is a list of already visited valves when crating a path
        let mut visited: Vec<String> = Vec::new();
        let mut paths: Vec<Vec<String>> = Vec::new();

        visited.push(self.current_valve.unwrap().name.clone());

        for n in self.get_possible_moves_from(self.current_valve.unwrap(), &mut visited)? {
            let tmp = self.get_possible_path_from(n, &mut visited.clone())?;
            paths.push(tmp);
        }

        Ok(paths)
    }

    fn get_possible_path_from(
        &'a self,
        from: &Valve,
        visited: &Vec<String>,
    ) -> Result<Vec<String>> {
        // visited is a list of already visited valves when crating a path
        let mut paths: Vec<String> = Vec::new();

        for n in self.get_possible_moves_from(from, &visited)? {
            let tmp = self.get_possible_path_from(n, &visited)?;
            // paths.push(tmp);
        }

        Ok(paths)
    }

    pub fn get_possible_moves_from(
        &self,
        start: &Valve,
        visited: &Vec<String>,
    ) -> Result<Vec<&Valve>> {
        let mut possible_tunnels = start
            .tunnels_to
            .iter()
            .map(|x| self.valves.get(x).unwrap())
            .filter(|x| !visited.contains(&x.name))
            .collect::<Vec<&Valve>>();

        Ok(possible_tunnels)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_possible_moves() -> Result<()> {
        let mut input = HashMap::new();
        input.insert(
            "AA".to_string(),
            Valve::new("AA", 10, vec!["BB".to_string(), "CC".to_string()]),
        );
        input.insert(
            "BB".to_string(),
            Valve::new("BB", 10, vec!["AA".to_string()]),
        );
        input.insert(
            "CC".to_string(),
            Valve::new("CC", 10, vec!["AA".to_string()]),
        );
        let mut hero: Hero = Hero::new(input.clone())?;
        hero.current_valve = Some(input.get("AA").unwrap());
        let result = hero.get_possible_moves_from(&input.get("AA").unwrap(), &vec![])?;

        assert_eq!(result.len(), 2);
        assert_eq!(result[0].name, "BB");
        assert_eq!(result[1].name, "CC");
        Ok(())
    }

    #[test]
    fn test_get_possible_moves_with_visited() -> Result<()> {
        let mut input = HashMap::new();
        input.insert(
            "AA".to_string(),
            Valve::new("AA", 10, vec!["BB".to_string(), "CC".to_string()]),
        );
        input.insert(
            "BB".to_string(),
            Valve::new("BB", 10, vec!["AA".to_string()]),
        );
        input.insert(
            "CC".to_string(),
            Valve::new("CC", 10, vec!["AA".to_string()]),
        );
        let mut hero: Hero = Hero::new(input.clone())?;
        hero.current_valve = Some(input.get("AA").unwrap());
        let result =
            hero.get_possible_moves_from(input.get("AA").unwrap(), &vec!["CC".to_string()])?;

        assert_eq!(result.len(), 1);
        assert_eq!(result[0].name, "BB");
        Ok(())
    }

    #[test]
    fn test_get_possible_paths() -> Result<()> {
        let mut input = HashMap::new();
        input.insert(
            "AA".to_string(),
            Valve::new("AA", 10, vec!["BB".to_string()]),
        );
        input.insert(
            "BB".to_string(),
            Valve::new("BB", 10, vec!["AA".to_string(), "CC".to_string()]),
        );
        input.insert(
            "CC".to_string(),
            Valve::new("CC", 10, vec!["BB".to_string()]),
        );
        let mut hero: Hero = Hero::new(input.clone())?;
        hero.current_valve = Some(input.get("AA").unwrap());

        let result = hero.get_possible_paths(vec![])?;
        assert_eq!(result.len(), 1);
        assert_eq!(result[0][0], "BB");
        assert_eq!(result[0][1], "CC");
        Ok(())
    }
}
