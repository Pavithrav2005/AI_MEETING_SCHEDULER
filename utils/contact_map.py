CONTACTS = {
    "deepak": "22am013@kpriet.ac.in",
    "pavi":"22am042@kpriet.ac.in"
}

def resolve_emails_from_names(names):
    return [CONTACTS[name] for name in names if name in CONTACTS]
