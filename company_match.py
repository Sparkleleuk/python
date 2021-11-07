from fuzzywuzzy import process, fuzz


def read_sp_file():
    lines = open("/Users/soviedo/Downloads/ACECPMASTER_ISSUER.PIP").readlines()
    issuers = []
    issuer_numbers = []
    for line in lines:
        parts = line.split("|")
        if len(parts) < 4:
            continue
        issuer_number, _, issuer = line.split("|")[0:3]
        issuer_numbers.append(issuer_number)
        issuers.append(issuer)

    return issuers, issuer_numbers

def find_issuers(query, issuers, issuer_numbers):
    results = process.extract(query, issuers, scorer=fuzz.ratio)
    highest_score = 0
    found_issuers = []
    for issuer, score in results:
        if score < 50:
            break
        issuer_number = issuer_numbers[issuers.index(issuer)]
        found_issuers.append((issuer, issuer_number, score))
        highest_score = score

    return found_issuers

def read_tcs_file():
    lines = open("/Users/soviedo/Downloads/uniqueDunsSet_updated.csv").readlines()
    companies = []
    for line in lines:
        parts = line.split(",")
        if len(parts) < 4:
            continue
        print(parts)
        company_name = parts[2]
        companies.append(company_name.strip())

    return companies


issuers, issuer_numbers = read_sp_file()
companies = read_tcs_file()
fout = open("/Users/soviedo/next2000_match_file.csv", "w")
for company_name in companies:
    results = find_issuers(company_name, issuers, issuer_numbers)
    for issuer, issuer_number, score in results:
        print(company_name)
        fout.write("{}|{}|{}|{}\n".format(company_name, issuer, issuer_number, score))
fout.close()

