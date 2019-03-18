from enum import Enum


class PersonGender(Enum):
    MALE = 1
    FEMALE = 2
    NON_BINARY = 3
    NOT_SPECIFIED = 4


class GroupOfAge(Enum):
    GROUP_18_24 = 1  # 18-24
    GROUP_25_34 = 2  # 25-34
    GROUP_35_44 = 3  # 35-44
    GROUP_45_54 = 4  # 45-54
    GROUP_55_64 = 5  # 55-64
    GROUP_65 = 6     # +65
    NOT_SPECIFIED = 7


class RestaurantType(Enum):
    MEXICAN = 1
    FRENCH = 2
    FAST_FOOD = 3
    VEGETARIAN = 4
    ITALIAN = 5
