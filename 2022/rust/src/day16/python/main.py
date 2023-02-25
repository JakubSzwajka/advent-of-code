import pytest
from typing import Dict


# key: 
MAX_PREASSURE_RELEASE_DATA = dict()

class Valve:
    def __init__(self, data:str):
        self.rate = int(data.split(';')[0].split('rate=')[1])        
        self.name = data.split(';')[0].split(' ')[1]        
        self.tunnels = data.split(';')[1].split('valves')[1].strip().split(', ')
        
        self.open = False 
        
    def __repr__(self) -> str:
        return f"{self.name} - {self.rate}"

def read_file(path): 
    with open(path, 'r') as f:
        txt = f.readlines()
    return txt

def prepare_valves(valves_data):
    valves = dict()
    for data in valves_data:
        v = Valve(data)
        valves[v.name] = v
    return valves

def get_max_preassure_release(name, valves: Dict[str, Valve], time_left, opened = [], depth = 0):
    """
        returns max preassure release for given valve in valves
        in time t
    """
    depth += 1
    print(f'{"--" * depth} Obtain max release preassure for {name} in t={time_left}.')
    t = time_left
    
    if t <= 0:
        return 0
    
    if (name, t) in MAX_PREASSURE_RELEASE_DATA.keys():
        print(f'Found ({name} for t={t}) in store: {MAX_PREASSURE_RELEASE_DATA[(name, t)]}')
        return MAX_PREASSURE_RELEASE_DATA[(name, t)]
    else:
        max_preassure_release = 0
        if t == 1 and not valves[name].open:
            max_preassure_release = valves[name].rate
            valves[name].open = True
            
        elif t == 1 and valves[name].open:
            # you cant release any preassure. 
            # You can only go into tunnel
            max_preassure_release = 0
        else: 
            if valves[name].rate == 0:
                max_preassure_release = max([ get_max_preassure_release(v, valves, t - 1, depth=depth) for v in valves[name].tunnels])
                print(f"{'--' * depth} Max from tunnels {valves[name].tunnels} in t={t} is {max_preassure_release}")
            else:
                x = max([ get_max_preassure_release(v, valves, t - 1, depth=depth) for v in valves[name].tunnels])
                print(f"{'--' * depth} Max from tunnels {valves[name].tunnels} in t={t} is {max_preassure_release}")
            # print(MAX_PREASSURE_RELEASE_DATA)
                max_preassure_release = x + get_max_preassure_release(name, valves, 1, depth=depth)

        print(f"{'--' * depth} Found max preassure to be released at {name} in t={t}. -> {max_preassure_release}")
        
        MAX_PREASSURE_RELEASE_DATA[(name, t)] = max_preassure_release
    
    # print(f"{'--' * depth} Max preassure to release at {name} in t={t} is {max_preassure_release}")
    return max_preassure_release

@pytest.mark.parametrize(
    'name, time, max_preassure_release',
    [
        # ('AA', 1, 0),
        # ('BB', 1, 13),
        
        ('HH', 2, 23),
        # ('BB', 3, 15),
        # ('AA', 2, 20),
    ]
)
def test_get_preassure_release(name, time, max_preassure_release):
    valves_data = read_file('./test.txt')
    valves = prepare_valves(valves_data)
    print('-------------------------------------')
    
    assert get_max_preassure_release(name, valves, time) == max_preassure_release
    
    

# if __name__ == "__main__":
#     valves_data = read_file('./test.txt')
#     valves = prepare_valves(Valve, valves_data)


#     print(valves)
    