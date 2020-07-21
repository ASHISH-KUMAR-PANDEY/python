import re
def syllabification(word):
    C = 'pbtdkgG?fvszSZxhcjmnrly'
    V = 'aAeiou'

    matches = re.match(
        '(['+C+']['+V+']['+C+']['+C+']|['+C+']['+V+']['+C+']|['+C+']['+V+'])?(['+C+']['+V+']['+C+']['+C+']|['+C+']['+V+']['+C+']|['+C+']['+V+'])?(['+C+']['+V+']['+C+']['+C+']|['+C+']['+V+']['+C+']|['+C+']['+V+'])', word).groups()

    resp1 = ""
    for match in matches:
        if match is not None:
            resp1 = resp1 + "." + match
    return resp1[1:]
