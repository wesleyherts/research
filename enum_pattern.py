from collections import namedtuple

from django_enumfield import enum


### Old Constant Classes ###
class UserRole:
    NONE = 0
    PATIENT = 1
    PROVIDER = 2
    EXECUTIVE = 3
    ADMIN = 99
    Choices = (
        (NONE, "-----"),
        (PATIENT, "Patient"),
        (PROVIDER, "Provider"),
        (EXECUTIVE, "Executive"),
        (ADMIN, "Admin"),
    )
    RoleMap = dict(Choices)


class ReviewSiteType:
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


### New Constant Classes ###
ValueSymbol = namedtuple("ValueSymbol", ["value", "description"])


class ForceEnum(ValueSymbol, enum.Enum):
    @classmethod
    def choices(cls):
        return cls.items()

    @classmethod
    def map(cls):
        return dict(value_pair for _, value_pair in cls.items())


# If numerical values are relevant to the enum #
class ForceUserRole(ForceEnum):
    NONE = 0, "----"
    PATIENT = 1, "Patient"
    PROVIDER = 2, "Provider"
    EXECUTIVE = 3, "Executive"
    ADMIN = 99, "Admin"


# If numerical values aren't relevant to the enum #
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


### Usage ###
print(ForceReviewSiteType.choices())
# [('GOOGLE', 'Google'), ('HEALTHGRADES', 'Healthgrades'), ('OTHER', 'Other'), ('RATEMDS', 'RateMds'), ('UCOMPARE_HEALTHCARE', 'Ucompare Healthcare'), ('VITALS', 'Vitals'), ('WEBMD', 'WebMD'), ('YELP', 'Yelp'), ('ZOCDOC', 'Zocdoc')]

print(ForceUserRole.choices())
# [('NONE', (0, '----')), ('PATIENT', (1, 'Patient')), ('PROVIDER', (2, 'Provider')), ('EXECUTIVE', (3, 'Executive')), ('ADMIN', (99, 'Admin'))]

print(ForceUserRole.map())
# {0: '----', 1: 'Patient', 2: 'Provider', 3: 'Executive', 99: 'Admin'}
