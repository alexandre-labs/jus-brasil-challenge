import enum
import typing as t

from pydantic import BaseModel, Schema


# Duplicated for now
RE_UNIFIED_YEAR_AND_JUS = r"^(?P<unif_year>[0-9]{7}\-[0-9]{2}\.[0-9]{4})\.[0-9]\.[0-9]{2}\.(?P<jurisdiction>[0-9]{4})$"  # noqa


class KnownCourts(str, enum.Enum):
    tjsp = "TJSP"
    tjms = "TJMS"


class Court(BaseModel):
    initials: KnownCourts


class Part(BaseModel):

    role: str
    identification: str


class Activity(BaseModel):
    date: str
    activity: str


class Process(BaseModel):

    number: str
    class_: str
    area: str
    subject: str
    distribution: str
    judge: str
    action: str
    parts: t.List[t.List[Part]]
    activities: t.List[Activity]

    class Config:
        fields = {"class_": "class"}


class QueryInput(BaseModel):

    process_number: str = Schema(  # type: ignore
        ..., title="O número do processo formatado", regex=RE_UNIFIED_YEAR_AND_JUS
    )

    process_court: KnownCourts = Schema(  # type: ignore
        ..., title="O tribunal relacionado"
    )


class QueryOutput(BaseModel):

    first_juristiction: Process

    second_juristiction: t.Optional[Process]

    second_jurisdiction_appeal: t.Optional[Process]
