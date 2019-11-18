from enum import Enum

# from django.db.models import SmallIntegerField


class CategoryPatientStatus:
    ALL_PATIENTS = 1
    CURRENT = 2


class OtherStatus:
    ONE = 1
    TWO = 2


class EnumPatientStatus(Enum):
    ALL_PATIENTS = 1
    CURRENT = 2


# this shows that enums are only equal to themselves so you can't have a mistaken comparison
print("Comparisons")
print(CategoryPatientStatus.ALL_PATIENTS == OtherStatus.ONE)
print(OtherStatus.ONE == EnumPatientStatus.ALL_PATIENTS)
print(CategoryPatientStatus.ALL_PATIENTS == EnumPatientStatus.ALL_PATIENTS)
print(EnumPatientStatus.ALL_PATIENTS == 1)

# don't need a Choices map if you name values differently
"""
Class ReviewSiteType:
    HEALTHGRADES = 1
    VITALS = 2
    GOOGLE = 3
    RATEMDS = 4
    ZOCDOC = 5
    UCOMPARE_HEALTHCARE = 6
    WEBMD = 7
    YELP = 8
    OTHER = 9

    Choices = (
        (HEALTHGRADES, "Healthgrades"),
        (VITALS, "Vitals"),
        (GOOGLE, "Google"),
        (RATEMDS, "RateMds"),
        (ZOCDOC, "Zocdoc"),
        (UCOMPARE_HEALTHCARE, "Ucompare Healthcare"),
        (WEBMD, "WebMD"),
        (YELP, "Yelp"),
        (OTHER, "Other"),
    )
"""

# Using an Enum
class ReviewSiteType(Enum):
    HEALTHGRADES = "Healthgrades"
    VITALS = "Vitals"
    GOOGLE = "Google"
    RATEMDS = "RateMds"
    ZOCDOC = "Zocdoc"
    UCOMPARE_HEALTHCARE = "Ucompare Healthcare"
    WEBMD = "WebMD"
    YELP = "Yelp"
    OTHER = "Other"


# Usage:
print("Choices Usage")
print(ReviewSiteType.__members__.items())
print(list(ReviewSiteType))
print([(item.name, item.value) for item in ReviewSiteType])


# Using a custom Enum
class ForceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class ForceReviewSiteType(ForceEnum):
    HEALTHGRADES = "Healthgrades"
    VITALS = "Vitals"
    GOOGLE = "Google"
    RATEMDS = "RateMds"
    ZOCDOC = "Zocdoc"
    UCOMPARE_HEALTHCARE = "Ucompare Healthcare"
    WEBMD = "WebMD"
    YELP = "Yelp"
    OTHER = "Other"


print("Custom Enum")
print(ForceReviewSiteType.choices())
