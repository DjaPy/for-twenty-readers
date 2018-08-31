YEAR = 1996
ONE_CONST = 19

def prav_version():
    a = YEAR % 19
    b = YEAR % 4
    c = YEAR % 7
    d = (ONE_CONST * a + 15) % 30
    e = (2 * b + 4 * c + 6 * d + 6) % 7
    march = 22 + d + e
    april = d + e - 9
    if march >= 0:
        grigorian = march + 13
    else:
        grigorian = april + 13
    print(march, april)
    print(grigorian)

def wiki_version():
    vernal_equinox = 1
    gold_g = (YEAR % ONE_CONST) + 1
    base_moon = (11 * gold_g) % 30
    new_moon = 30 - base_moon
    full_moon = new_moon + 14
    if new_moon < vernal_equinox:
        day = full_moon + 30
    if new_moon


if __name__ == '__main__':
    print(wiki_version())
