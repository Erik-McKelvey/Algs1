from ..models import TimeBlock

def validate_schedule(schedule):
    ''' Takes a schedule in the following format:
    {
        “year”: 2019,
        “terms”: [
            {
                ...
            }
        ]
    }
    '''
    for term in schedule['terms']:
        res = validate_term(term)
    pass

def validate_term(term):
    ''' Takes a term in the following format:
    {
        “term”: “summer”,
        “courses”: [
            {
                “course”: “CSC110”,
                “sections”: [
                    {
                        "num": “A01”,
                        “building”: “ECS125”,
                        “professor”: “Rich.Little”,
                        “days”: [“M”, ”R”],
                        “num_seats”: 120,
                        “start_time”: “08:30”, // 24hr time
                        “end_time”: “09:50”
                    }
                ]
            }
            ]
        }
    '''
    buildings = {}
    professors = {}
    for course in term['courses']:
        res = validate_course(course)
        for section in course['sections']:
            res = validate_section(section)
            if section['building'] not in buildings:
                buildings[section['building']] = 1
            else:
                buildings[section['building']] += 1
            if section['professor'] not in professors:
                professors[section['professor']] = 1
            else:
                professors[section['professor']] += 1

    
