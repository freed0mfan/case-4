# case-study #4
# Developers: Markelov E., Sokolova S.

import ru_local as ru

yes = ru.YES
no = ru.NO
banned = ru.BANNED


def in_ban():
    print(ru.WORKED_IN_BANNED)
    for i in range(len(banned)):
        print(f'{i + 1}. {banned[i]}')
    ans = input(ru.YES_NO)
    return ans == yes


def should_describe():
    return part_of_regime == yes or beneficiary == yes or criminal == yes


def war_participation():
    military = input(ru.MILITARY)
    if military == yes:
        war = 1
    elif military == no:
        civil = input(ru.CIVIL)
        if civil == yes:
            war = 0.1
        elif civil == no:
            propaganda = input(ru.PROPAGANDA)
            if propaganda == yes:
                war = 0.6
            elif propaganda == no:
                war = 0
    return war


def crimes_commited():
    return int(criminal == yes)


def criminal_resource():
    criminal_role = int(input(ru.CRIMINAL_ROLE))
    match criminal_role:
        case 1:
            resource = 1
        case 2:
            resource = 0.5
        case 3:
            resource = 0.1
    return resource


def was_against():
    sabotage = input(ru.SABOTAGE)
    return int(sabotage == yes)


def helped_justice():
    cooperation = input(ru.DEAL)
    return int(cooperation == yes)


def helped_protest():
    changes = input(ru.CHANGES)
    return int(changes == yes)


def recommend_lustration():
    responsibility = 0.5 * war_participation() + 0.5 * crimes_commited() * criminal_resource() - 0.3 * was_against() - 0.1 * helped_justice() - 0.1 * helped_protest()
    if 0 <= responsibility < 0.5:
        print(f'{ru.RESPONSIBILITY} {round(responsibility, 2)}. {ru.NOT_RECOMMENDED}')
    elif 0.5 <= responsibility:
        print(f'{ru.RESPONSIBILITY} {round(responsibility, 2)}. {ru.RECOMMENDED}')


part_of_regime = input(ru.PART_OF_REGIME)
beneficiary = input(ru.BENEFICIARY)
criminal = input(ru.CRIMINAL)


def main():
    match in_ban():
        case True:
            print(ru.MUST_BE_LUSTRATED)
        case False:
            match should_describe():
                case False:
                    print(ru.NOT_CONNECTED)
                case True:
                    recommend_lustration()


if __name__ == '__main__':
    main()
