import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def csv_escape(text):
    return '"{}"'.format(text.replace('"', '""'))


def solve_case():
    import csv
    
    serial = {}
    parents = {}
    
    data = csv.reader(sys.stdin)
    for row in data:
        id, name, acronym, p_code, code, t = row
        if acronym == '':
            continue
        
        if t == "IEEE Event":
            serial[id] = (name, acronym, p_code, code)
        else:
            parents[id] = (name, acronym, p_code, code)

    banned = set()
    
    acronyms = {}
    for event_id, (name, acronym, p_code, code) in parents.items():
        if acronym in acronyms:
            banned.add(acronyms[acronym])
            banned.add(event_id)
        else:
            acronyms[acronym] = event_id
    
    serializations = {}
    parent_codes = {}
    for event_id, (name, acronym, p_code, code) in serial.items():        
        if not acronym in acronyms:
            continue
        
        parent_id = acronyms[acronym]
        if parent_id in banned:
            continue
        
        if parent_id not in serializations:
            serializations[parent_id] = [event_id]
            parent_codes[parent_id] = code
        else:
            parent_codes[parent_id] = "???" if code != parent_codes[parent_id] else code
            serializations[parent_id].append(event_id)
    
    
    for acronym in sorted(list(acronyms.keys())):
        event_id = acronyms[acronym]
        if event_id in banned or event_id not in serializations:
            continue
        
        name, acronym, p_code, code = parents[event_id]
        print(event_id, csv_escape(name), csv_escape(acronym), p_code, parent_codes[event_id], '"Parent Event"', sep=',')
        
        for child in sorted(serializations[event_id], key= lambda x: (serial[x][0], x)):
            name, acronym, p_code, code = serial[child]
            print(child, csv_escape(name), csv_escape(acronym), p_code, code, '"IEEE Event"', event_id, sep=',')
                

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
