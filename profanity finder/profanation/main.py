from profanation import profanity

def main(nid,text):
    if profanity.contains_profanity(text):
        not_id = nid
    else:
        not_id = None
    return not_id

