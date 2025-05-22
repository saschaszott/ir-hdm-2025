import textdistance
import jellyfish
import phonetics
import cologne_phonetics

if __name__ == "__main__":

    word1 = input("Erstes Wort: ").strip()
    word2 = input("Zweites Wort: ").strip()

    # Levenshtein
    lev_distance = textdistance.levenshtein.distance(word1, word2)
    lev_similarity = textdistance.levenshtein.similarity(word1, word2)
    print(f"\nLevenshtein-Distanz: {lev_distance}")
    print(f"Levenshtein-Ähnlichkeit: {lev_similarity}")

    # Damerau-Levenshtein
    damerau_distance = textdistance.damerau_levenshtein.distance(word1, word2)
    damerau_similarity = textdistance.damerau_levenshtein.similarity(word1, word2)
    print(f"\nDamerau-Levenshtein-Distanz: {damerau_distance}")
    print(f"Damerau-Levenshtein-Ähnlichkeit: {damerau_similarity}")

    # Jaro-Winkler
    jaro_winkler = jellyfish.jaro_winkler_similarity(word1, word2)
    print(f"\nJaro-Winkler-Ähnlichkeit (normiert): {jaro_winkler:.4f}")

    # Soundex
    soundex1 = jellyfish.soundex(word1)
    soundex2 = jellyfish.soundex(word2)
    print(f"\nSoundex({word1}) = {soundex1}")
    print(f"Soundex({word2}) = {soundex2}")
    print("Soundex gleich:", soundex1 == soundex2)

    # Metaphone Phonetik
    mp1 = phonetics.metaphone(word1)
    mp2 = phonetics.metaphone(word2)
    print(f"\nMetaphone({word1}) = {mp1}")
    print(f"Metaphone({word2}) = {mp2}")
    print("Metaphone gleich:", mp1 == mp2)

    # Kölner Phonetik
    kp1 = cologne_phonetics.encode(word1)
    kp2 = cologne_phonetics.encode(word2)
    print(f"\nKölnerPhonetik({word1}) = {kp1}")
    print(f"KölnerPhonetik({word2}) = {kp2}")
    print("Kölner Phonetik gleich:", cologne_phonetics.compare(word1, word2))

