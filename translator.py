# This practical program is organised by <<Kasra Tookallo>>
#---------------------------------------------------------------------------------------------


def main():
    # Read number of dictionary entries
    n = int(input().strip())

    # Build mapping dictionary: target word -> source word
    mapping = {}
    for _ in range(n):
        parts = input().strip().split()
        source = parts[0]
        eng = parts[1].replace(" ", "")
        fr = parts[2].replace(" ", "")
        de = parts[3].replace(" ", "")
        mapping[eng] = source
        mapping[fr] = source
        mapping[de] = source

    # Read sentence to translate
    sentence = input().strip().split()

    # Translate each token
    translated = []
    for token in sentence:
        key = token.replace(" ", "")
        if key in mapping:
            translated.append(mapping[key])
        else:
            translated.append(token)

    # Output final translated sentence
    print(" ".join(translated))


if __name__ == "__main__":
    main()


""" 
'Copy and paste' the following example in Entry:
10
razi content none zufrieden
az with none mit
zendegi life none Leben
in the none das
be in none auf
man I je ich
hastam am none bin
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am interested in programming


Output:
man hastam alaghemand be barnamenevisi
"""